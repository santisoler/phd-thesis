from numba import njit
import boule as bl
import verde as vd
import harmonica as hm

# Utilizamos Boule para obtener el radio medio del elipsoide WGS84
radio_medio = bl.WGS84.mean_radius

# Definimos un teseroide cuya superficie superior se encuentra en el
# radio medio del elipsoide, posee un espesor de 10km y dimensiones
# latitudinales y longitudinales de 10 grados por 10 grados.
teseroide = [-70, -60, -40, -30, radio_medio - 10e3, radio_medio]

# Definimos una densidad lineal para este teseroide.
@njit
def densidad(radio):
    """Funcion de densidad lineal"""
    radio_superior = radio_medio
    radio_inferior = radio_medio - 10e3
    densidad_superior = 2670
    densidad_inferior = 3000
    slope = (
        (densidad_superior - densidad_inferior)
        / (radio_superior - radio_inferior)
    )
    return slope * (radio - radio_inferior) + densidad_inferior


# Definimos puntos de computo en una grilla regular a 100km por
# encima del radio medio del elipsoide
coordenadas = vd.grid_coordinates(
    region=[-80, -40, -50, -10],
    shape=(80, 80),
    extra_coords=100e3 + radio_medio,
)

# Calculamos la componente radial de la aceleracion gravitatoria
# que genera el teseroide
gravity = hm.tesseroid_gravity(
    coordenadas, teseroide, densidad, field="g_z"
)
