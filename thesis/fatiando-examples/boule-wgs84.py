import boule
import verde as vd

# Obtenemos el elipsoide WGS84
elipsoide = boule.WGS84

# Generamos una grilla de puntos de observacion en coordenadas geodesicas
# ubicados a una altitud geometrica de 150 metros
region = (-170, 180, -90, 90)
longitud, latitud, altitud = vd.grid_coordinates(
    region=region, spacing=10, extra_coords=150
)

# Calculamos la gravedad sobre estos puntos
gravedad_normal = elipsoide.normal_gravity(latitud, altitud)

# Convertimos estos puntos a coordenadas esfericas geocentricas
longitud, latitud_sph, radio = elipsoide.geodetic_to_spherical(
    longitud, latitud, altitud
)
