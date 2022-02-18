# Metodologías y herramientas computacionales para el procesamiento y modelado de datos gravimétricos

Tesis Doctoral para optar por el título de Doctor en Geofísica en la
[Facultad de Ciencias Exactas, Físicas y Naturales](http://exactas.unsj.edu.ar/)
de la
[Universidad Nacional de San Juan](http://www.unsj.edu.ar).

| Información  |           |
|--------------|-----------|
| Título   | _Metodologías y herramientas computacionales para el procesamiento y modelado de datos gravimétricos_ |
| Autor    | [Santiago Soler](https://www.santisoler.com)<sup>1,2</sup> |
| Director | Mario E. Gimenez<sup>1,2</sup>  |
| Co-Director | [Leonardo Uieda](https://www.leouieda.com)<sup>3</sup> |
| DOI      | [10.6084/m9.figshare.16906909](https://doi.org/10.6084/m9.figshare.16906909) |
| Licencia | [Creative Commons Atribución 4.0 Internacional][cc-by] |
|          | [**Descargar la Tesis**](https://doi.org/10.6084/m9.figshare.16906909) |

> <sup>1</sup> CONICET, Argentina<br/>
> <sup>2</sup> Instituto Geofísico Sismológico Volponi, Universidad Nacional de San Juan,
> Argentina<br>
> <sup>3</sup> Department of Earth, Ocean and Ecological Sciences, School of Environmental Sciences, University of Liverpool, UK


## Resumen

En esta Tesis presentamos dos nuevas metodologías para el modelado
y procesamiento de datos gravimétricos.
La primera consiste en un método para el modelado directo de los campos
gravitatorios generados por teseroides de densidades que varían de manera
continua en la dirección radial.
Este resuelve las integrales volumétricas involucradas mediante una Cuadratura
de Gauss-Legendre junto a un algoritmo de discretización adaptativa
bidimensional y un nuevo algoritmo de discretización basado en la densidad.
La segunda metodología consiste en las _fuentes equivalentes potenciadas por
gradiente_, las cuales permiten realizar interpolaciones y continuaciones
ascendentes de grandes cantidades de datos gravimétricos mediante la técnica de
fuentes equivalentes en conjunto con un algoritmo de potenciación del
gradiente.
Ambas metodologías fueron aplicadas sobre datos reales: se utilizó el nuevo
modelo directo de teseroides para modelar la Cuenca Neuquina (Argentina) con un
perfil de densidad exponencial, y mediantes las fuentes equivalentes
potenciadas por el gradiente conseguimos grillar un conjunto de más de 1.7
millones de datos de gravedad sobre la superficie de Australia.
Por último, presentamos un recorrido sobre el desarrollo del proyecto de
software de código abierto para Geofísica: Fatiando a Terra.
Recorremos su historia, describimos los paquetes que forman parte del proyecto
y enumeramos las mejores prácticas que se aplican para poder desarrollarlas.
Además intentamos evaluar qué impacto posee el proyecto sobre la comunidad
geocientista internacional, cómo los y las integrantes de la comunidad de
Fatiando a Terra interactúan entre sí y cómo lo hacen con las otras comunidades
de software científico.


## Publicaciones relacionadas

Las dos metodologías que se presentan en la Tesis han sido publicadas tras su
correspondiente proceso de revisión por pares en [_Geophysical Journal
International_](https://academic.oup.com/gji/):

- Soler, S. R., Pesce, A., Gimenez, M. E., & Uieda, L. (2019).
  _Gravitational field calculation in spherical coordinates using variable
  densities in depth_.
  Geophysical Journal International.
  doi: [10.1093/gji/ggz277](https://doi.org/10.1093/gji/ggz277)
- Soler, S.R. and Uieda, L. (2021).
  _Gradient-boosted equivalent sources_.
  Geophysical Journal International.
  doi: [10.1093/gji/ggab297](https://doi.org/10.1093/gji/ggab297)

Además, algunas de los paquetes del proyecto Fatiando a Terra han sido
publicados en el [_Journal of Open Source Software_](https://joss.theoj.org/):

- Uieda, L., Soler, S.R., Rampin, R., van Kemenade, H., Turk, M., Shapero, D.,
  Banihirwe, A., and Leeman, J. (2020).
  _Pooch: A friend to fetch your data files_.
  Journal of Open Source Software, 5(45), 1943.
  doi: [10.21105/joss.01943](https://doi.org/10.21105/joss.01943)
- Uieda, (2018).
  _Verde: Processing and gridding spatial data using Green’s
  functions_.
  Journal of Open Source Software, 3(30), 957,
  doi: [10.21105/joss.00957](https://doi.org/10.21105/joss.00957)


## Cómo citar

Cita en texto:

> Soler, S.R. (2022).
> Metodologías y herramientas computacionales para el procesamiento y modelado
> de datos gravimétricos.
> Tesis Doctoral, Universidad Nacional de San Juan, Argentina.
> doi: 10.6084/m9.figshare.16906909

Usando BibTeX:

```
@phdthesis{soler2022,
  author  = {Santiago Rub{\'e}n Soler},
  title   = {Metodolog{\'i}as y herramientas computacionales para el
        procesamiento y modelado de datos gravim{\'e}tricos},
  school  = {Universidad Nacional de San Juan, Argentina},
  year    = {2022},
  type    = {PhD Thesis},
  doi     = {10.6084/m9.figshare.16906909}
}
```

## Versiones

- [PDF de la versión en desarrollo en rama `main`](https://github.com/santisoler/phd-thesis/raw/pdf/thesis.pdf)
- [`v1.1.1`](https://github.com/santisoler/phd-thesis/releases/tag/v1.1.1): Versión corregida luego de la revisión por parte del Jurado, con una correción menor.
- [`v1.1.0`](https://github.com/santisoler/phd-thesis/releases/tag/v1.1.0): Versión corregida luego de la revisión por parte del Jurado
- [`v1.0.0`](https://github.com/santisoler/phd-thesis/releases/tag/v1.0.0): Versión enviada para su evaluación ([descargar el PDF](https://github.com/santisoler/phd-thesis/releases/download/v1.0.0/thesis.pdf))
- [`v0.1.0`](https://github.com/santisoler/phd-thesis/releases/tag/v0.1.0): Primer borrador ([descargar el PDF](https://github.com/santisoler/phd-thesis/releases/download/v0.1.0/thesis.pdf))

## Licencia

Esta obra está bajo una
[Licencia Creative Commons Atribución 4.0 Internacional][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: https://creativecommons.org/licenses/by/4.0/deed.es
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
