import pyproj
import boule as bl
import harmonica as hm

# Descargamos datos de muestra: mediciones de aceleracion
# de la gravedad sobre Sudafrica
datos = hm.datasets.fetch_south_africa_gravity()

# Proyectamos los datos en coordenadas planas
proyeccion = pyproj.Proj(proj="merc", lat_ts=datos.latitude.mean())
easting, northing = proyeccion(
    datos.longitude.values, datos.latitude.values
)
coordenadas = (easting, northing, datos.elevation)

# Calculamos el disturbio de gravedad, quitando la gravedad normal
elipsoide = bl.WGS84
disturbio = (
    datos.gravity 
    - elipsoide.normal_gravity(datos.latitude, datos.elevation)
)

# Inicializamos las fuentes equivalentes
# Usaremos fuentes promedidas por bloque (con bloques de 2km x 2km),
# y ventanas de 100km x 100km.
fuentes_equivalentes = hm.EquivalentSourcesGB(
    depth=9e3,  # profundidad de las fuentes
    damping=10,  # parametro de amortiguamiento
    window_size=100e3,
    block_size=2e3,
    random_state=42,
)

# Ajustamos los coeficientes de las fuentes a los datos mediante
# potenciacion de gradiente
fuentes_equivalentes.fit(coordenadas, disturbio)

# Interpolamos los datos sobre una grilla regular de 2km de espaciado
# a una altitud de 1km
grilla = fuentes_equivalentes.grid(
    upward=1000,
    spacing=2e3,
    data_names="disturbio_de_gravedad",
)
