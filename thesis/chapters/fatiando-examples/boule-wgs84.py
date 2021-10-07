import boule

# Definimos el elipsoide WGS84
WGS84 = boule.Ellipsoid(
    name="WGS84",
    semimajor_axis=6378137,
    flattening=1 / 298.257223563,
    geocentric_grav_const=3986004.418e8,
    angular_velocity=7292115e-11,
)
