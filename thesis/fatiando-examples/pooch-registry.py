import pooch

# Inicializamos una instancia de la clase pooch.Pooch
odie = pooch.create(
    # Utilizamos el directorio cache por defecto de nuestro sistema operativo
    path=pooch.os_cache("my-project"),
    # Definimos la direccion base donde se encuentran los archivos a descargar
    base_url="https://www.somewebpage.org/science/data/",
    # Especificamos los archivos a descargar en el registro
    registry={
        "temperature.csv": "sha256:19uheidhlkjdwhoiwuhc0uhcwljchw9ochwochw89dcgw9dcgwc",
        "gravity-disturbance.nc": "sha256:1upodh2ioduhw9celdjhlfvhksgdwikdgcowjhcwoduchowjg8w",
    },
)

# Solicitamos la descarga de uno de los archivos
file_path = odie.fetch("gravity-disturbance.nc")
