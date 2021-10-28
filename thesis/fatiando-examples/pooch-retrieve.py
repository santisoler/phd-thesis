import pooch

# Usamos la funcion retrieve() para decargar un unico archivo en
# el directorio de cache por defecto de nuestro sistema operativo
file_path = pooch.retrieve(
    # Especificamos la ubicacion del archivo a descargar
    url="https://github.com/fatiando/pooch/raw/v1.0.0/data/tiny-data.txt",
    # Y su suma de verificacion
    known_hash="md5:70e2afd3fd7e336ae478b1e740a5f08e",
)
