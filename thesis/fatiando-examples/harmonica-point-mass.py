import verde as vd
import harmonica as hm

# Definimos las coordenadas de dos masa puntuales debajo de la superficie (en metros)
easting = [500, 1500]
northing = [700, 1300]
upward = [-50, -100]
points = (easting, northing, upward)

# Definimos las masas de cada una de ellas (en unidades SI)
masses = [3e11, -10e11]

# Definimos una grilla regular de puntos de observacion (50 metros sobre la superficie)
coordinates = vd.grid_coordinates(
    region=(0, 2000, 0, 2000), shape=(100, 100), extra_coords=50
)

# Calculamos la componente vertical (hacia abajo) de la aceleracion gravitatoria
gravity = hm.point_mass_gravity(
    coordinates, points, masses, field="g_z", coordinate_system="cartesian"
)
