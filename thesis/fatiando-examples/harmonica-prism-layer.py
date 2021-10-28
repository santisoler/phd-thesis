import pyproj
import verde as vd
import harmonica as hm

# Cargamos datos de topografia sobre Sudafrica
sudafrica_topo = hm.datasets.fetch_south_africa_topography()

# Proyectamos la grilla en coordenadas planas
projection = pyproj.Proj(
    proj="merc",
    lat_ts=sudafrica_topo.latitude.values.mean(),
)
sudafrica_topo = vd.project_grid(
    sudafrica_topo.topography,
    projection=projection,
)

# Construimos un arreglo 2D de densidades para los prismas.
# Cada valor de topografia positiva le asigna una densidad de 2670 kg/m3
# al prisma correspondiente.
# Cada valor de topografia negativa le asigna un contraste de densidad
# de 1000 kg/m3 - 2900 kg/m3.
densidad = sudafrica_topo.copy()
densidad.values[:] = 2670.0
densidad = densidad.where(sudafrica_topo >= 0, 1000 - 2900)

# Construimos la capa de prismas
prismas = hm.prism_layer(
    (sudafrica_topo.easting, sudafrica_topo.northing),
    surface=sudafrica_topo,
    reference=0,
    properties={"density": densidad},
)

# Construimos una grilla de puntos de observacion a 4000m s/el elipsoide
coordinates = vd.grid_coordinates(
    region=(12, 33, -35, -18), spacing=0.2, extra_coords=4000
)
easting, northing = projection(*coordinates[:2])
coordinates_projected = (easting, northing, coordinates[-1])

# Calculamos el efecto gravitatorio de los prismas sobre la grilla
g_z = prismas.prism_layer.gravity(coordinates_projected, field="g_z")
