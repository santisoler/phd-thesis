<!-- .slide: class="slide-title" -->

<h1>
Metodologías y herramientas computacionales para el
procesamiento y modelado de datos gravimétricos
</h1>

<hr>

<h2>
<a href="https://www.santisoler.com">
Lic. Santiago Soler
</a>
</h2>

<div class="container">
<div class="column">
<h3> Dr. Mario E. Gimenez</h3>
<p> <em>Director</em> </p>
</div>
<div class="column">
<h3> <a href="https://www.leouieda.com">Dr. Leonardo Uieda</a> </h3>
<p> <em>Codirector</em> </p>
</div>
</div>

<div class="container logos">
<div class="logo">
<a href="https://www.conicet.gov.ar/">
<img src="images/logos/conicet.svg">
</a>
</div>
<div class="logo">
<a href="https://www.unsj.edu.ar/">
<img src="images/logos/unsj.svg">
</a>
</div>
<div class="logo">
<a href="http://igsv.unsj.edu.ar/">
<img src="images/logos/igsv.svg">
</a>
</div>
</div>

---

## Contenido

1. Introducción
1. Teseroides densidad variable
1. Fuentes equivalentes potenciadas por gradiente
1. Fatiando a Terra
1. Conclusiones

---

<!-- .slide: data-background-color="#2b2b2b" -->

# Introducción

---

<!-- .slide: data-background-color="#2b2b2b" -->

# Teseroides de densidad variable

---

## ¿Qué es un teseroide?

---

<img src="images/tesseroids/tesseroid-definition.svg" alt="Teseroide en un sistema de referencia con sus límites latitudinales, longitudinales y radiales" style="width: 50%" >

---

## Problema

---

### Campos gravitatorios

$$
    V(\mathbf{p}) = G \rho
        \int\limits_{r_1}^{r_2}
        \int\limits_{\lambda_1}^{\lambda_2}
        \int\limits_{\phi_1}^{\phi_2}
        \frac{\kappa}{\left\lVert \mathbf{p} - \mathbf{q} \right\rVert}
        \text{d} r' \text{d} \lambda' \text{d} \phi',
$$

No poseen solución analítica

---

## Solución

---

### Cuadratura de Gauss-Legendre

<div class="container container-70">

<div class="column">
$$
V(\mathbf{p}) \cong
G \rho
A
\sum\limits_{i=1}^{N_r}
\sum\limits_{j=1}^{N_\lambda}
\sum\limits_{k=1}^{N_\phi}
W_{ijk}
\frac{\kappa_{ik}}{\left\lVert \mathbf{p} - \mathbf{q}_{ijk} \right\rVert}
$$
</div>

<div class="column">
<img src="images/tesseroids/tesseroid-glq.svg" alt="Teseroide con cuatro masas puntuales en su interior, representando cómo la Cuadratura de Gauss-Legendre lo aproxima por ellas." style="width: 70%" >
</div>

</div>

Aproxima el teseroide por masas puntuales

---

<i class='fas fa-arrow-circle-up'></i> Orden de la Cuadratura
$ \Rightarrow $
<i class='fas fa-arrow-circle-up'></i> Precisión


<p class="fragment" style="margin-top: 100px">
Pero... $ \mathcal{O}(n^3) $ 😞
</p>

---

<img src="images/tesseroids/tesseroid-computation-point.svg" alt="Teseroide y punto de
cómputo, con una recta a trazos que ilustra la distancia que los separa"
style="width: 40%;">

<i class='fas fa-arrow-circle-up'></i> Distancia a punto de cómputo
$ \Rightarrow $
<i class='fas fa-arrow-circle-up'></i> Precisión

---

## Discretización adaptativa

---

<div class="r-stack">
<img class="fragment fade-out" data-fragment-index="0" src="images/tesseroids/adaptive-discretization-step0.svg" alt="Teseroide y punto de cómputo" style="width: 40%;">
<img class="fragment current-visible" data-fragment-index="0" src="images/tesseroids/adaptive-discretization-step1.svg" alt="Teseroide subdividido en 4 teseroides por el algoritmo de discretización adaptativa" style="width: 40%;">
<img class="fragment" src="images/tesseroids/adaptive-discretization-step2.svg" alt="Teseroide subdividido en 7 teseroides por el algoritmo de discretización adaptativa" style="width: 40%;">
</div>

<p class="fragment fade-in">
Masas puntuales donde más se necesitan
</p>

---

# Teseroides de densidad variable

---

<div>
$$
    V(\mathbf{p}) = G \color{#e4564a}{\rho}
        \int\limits_{r_1}^{r_2}
        \int\limits_{\lambda_1}^{\lambda_2}
        \int\limits_{\phi_1}^{\phi_2}
        \frac{\kappa}{\left\lVert \mathbf{p} - \mathbf{q} \right\rVert}
        \text{d} r' \text{d} \lambda' \text{d} \phi',
$$
</div>

<div class="fragment">
<i class="fas fa-arrow-down"></i>

$$
    V(\mathbf{p}) = G
        \int\limits_{r_1}^{r_2}
        \int\limits_{\lambda_1}^{\lambda_2}
        \int\limits_{\phi_1}^{\phi_2}
        \color{#e4564a}{\rho(r')}
        \frac{\kappa}{\left\lVert \mathbf{p} - \mathbf{q} \right\rVert}
        \text{d} r' \text{d} \lambda' \text{d} \phi',
$$
</div>

---

## Desafío

Función densidad en la aproximación numérica

---

### Discretización basada en densidad

---

<div class="r-stack">
<img class="fragment fade-out" data-fragment-index="0" src="images/tesseroids/density-based-discretization-step0.svg" style="width: 60%;">
<img class="fragment current-visible" data-fragment-index="0" src="images/tesseroids/density-based-discretization-step1.svg" style="width: 60%;">
<img class="fragment current-visible" src="images/tesseroids/density-based-discretization-step2.svg" style="width: 60%;">
<img class="fragment current-visible" src="images/tesseroids/density-based-discretization-step3.svg" style="width: 60%;">
<img class="fragment current-visible" src="images/tesseroids/density-based-discretization-step4.svg" style="width: 60%;">
<img class="fragment current-visible" src="images/tesseroids/density-based-discretization-step5.svg" style="width: 60%;">
<img class="fragment" src="images/tesseroids/density-based-discretization-step6.svg" style="width: 60%;">
</div>

---

### Discretización adaptativa bidimensional

---

<div class="r-stack">
<img class="fragment fade-out" data-fragment-index="0" src="images/tesseroids/density-based-plus-adaptive-discret-step0.svg" style="width: 40%;">
<img class="fragment current-visible" data-fragment-index="0" src="images/tesseroids/density-based-plus-adaptive-discret-step1.svg" style="width: 40%;">
<img class="fragment current-visible" src="images/tesseroids/density-based-plus-adaptive-discret-step2.svg" style="width: 40%;">
<img class="fragment current-visible" src="images/tesseroids/density-based-plus-adaptive-discret-step3.svg" style="width: 40%;">
<img class="fragment" src="images/tesseroids/density-based-plus-adaptive-discret-step4.svg" style="width: 40%;">
</div>

---

### Cuadratura de Gauss-Legendre


<div class="container container-70">

<div class="column">
$$
V(\mathbf{p}) \cong
G
A
\sum\limits_{i=1}^{2}
\sum\limits_{j=1}^{2}
\sum\limits_{k=1}^{2}
W_{ijk}
\frac{\color{#e4564a}{\rho(r_i)}\kappa_{ik}}{\left\lVert \mathbf{p} - \mathbf{q}_{ijk} \right\rVert}
$$

</div>

<div class="column">
<img src="images/tesseroids/tesseroid-small-glq.svg" style="width: 70%" >
</div>

</div>

Aplicada sobre cada teseroide pequeño

---

### Resumen del nuevo método

1. Discretización basada en densidad
2. Discretización adaptativa bidimensional
3. Cuadratura Gauss-Legendre

---

## Precisión y tiempo de cómputo

---

<div class="container container-70">

<div class="column">

Discretización basada en densidad

<i class='fas fa-arrow-down'></i>

<p style="font-size: 5rem;">
$\delta$
</p>

</div>

<div class="column">

Discretización adaptativa bidimensional

<i class='fas fa-arrow-down'></i>

<p style="font-size: 5rem;">
$D$
</p>

</div>

</div>

$D$ y $\delta$ controlan la **cantidad de subdivisiones**

---

<div class="container container-70">

<div class="col-3" style="text-align: right">
<i class='fas fa-arrow-circle-up'></i> Subdivisiones
</div>

<div class="column">
$\Rightarrow$
</div>

<div class="col-3" style="text-align: left">

<i class='fas fa-arrow-circle-up' style="color: #50a14f;"></i> Precisión

<i class='fas fa-arrow-circle-up' style="color : #e4564a;"></i> Tiempo de cómputo

</div>

</div>

---

## Determinación de $D$ y $\delta$

---

### Comparaciones con soluciones analíticas <br>para cascarones esféricos

<img src="images/tesseroids/d-delta-grid-search.svg" style="width: 90%;">

---

### Valores óptimos para $D$ y $\delta$:

- $D = 1$ para potencial $V$
- $D = 2.5$ para aceleración $\mathbf{g}$
- $\delta = 0.1$

🎉 Garantizan **errores** por **debajo del 1%** 🎉

---

# Aplicación a la Cuenca Neuquina

---

### Cuencas sedimentarias de gran tamaño

- Sedimentos con **compactación**
- **Curvatura del planeta** por su gran extensión

---

## Modelo de la cuenca Neuquina


<img src="./images/tesseroids/cuenca-neuquina-espesor.svg" style="width: 70%;">

---

## Campos gravitatorios del modelo


<img src="./images/tesseroids/cuenca-neuquina-resultados.svg" style="width: 70%;">

---

## Diferencias con densidad constante


<img src="./images/tesseroids/cuenca-neuquina-diff.svg" style="width: 70%;">

---

<!-- .slide: data-background-color="#2b2b2b" -->

# Fuentes equivalentes <br> potenciadas por gradiente

---

## ¿Qué son las fuentes equivalentes?

---


### Datos gravimétricos

<img src="./images/equivalent-sources/surveys-cartoon.svg" style="width: 70%">

---

<div class="container">

<div class="column">

Muestras sobre terreno

<img src="./images/equivalent-sources/ground_survey.svg" style="width: 50%;
height: auto;">
</div>

<div class="column">

Muestras aéreas

<img src="./images/equivalent-sources/airborne_survey.svg" style="width: 50%;
height: auto;">

</div>

</div>

---

### Interpolación

<img src="./images/equivalent-sources/simple-gridding.svg" style="width: 50%;
height: auto;">

---


### Interpoladores 2D de propósito general


<div class="container container-70" style="margin-top: 3rem;">

<div class="column fragment">
<img src="./images/equivalent-sources/not-function-of-height.svg" style="width: 40%;">
</div>

<div class="column fragment">
<img src="./images/equivalent-sources/not-harmonic.svg" style="width: 40%;">
</div>

</div>

---

### Fuentes equivalentes

---

<div class="r-stack">
<img class="fragment fade-out" data-fragment-index="0" src="./images/equivalent-sources/equivalent-sources-step0.svg" style="width: 60%">
<img class="fragment current-visible" data-fragment-index="0" src="./images/equivalent-sources/equivalent-sources-step1.svg" style="width: 60%">
<img class="fragment" src="./images/equivalent-sources/equivalent-sources-step2.svg" style="width: 60%">
</div>

---

### Ventajas

<div class="container container-70" style="margin-top: 3rem;">

<div class="column fragment">
<img src="./images/equivalent-sources/function-of-height.svg" style="width: 40%;">
</div>

<div class="column fragment">
<img src="./images/equivalent-sources/harmonic-field.svg" style="width: 40%;">
</div>

</div>

---

### Problema

<div class="r-stack">
<img class="fragment fade-out" data-fragment-index="0" src="./images/equivalent-sources/equivalent-sources-out-of-memory-0.svg" style="width: 60%">
<img class="fragment" data-fragment-index="0" src="./images/equivalent-sources/equivalent-sources-out-of-memory-1.svg" style="width: 60%">
</div>

---

### Solución

---

# Fuentes equivalentes <br> potenciadas por gradiente

---

## Potenciación del gradiente


<div class="container container-60" style="margin-top: 5rem;">

<div class="col-3" >

$$ \mathbf{d} = \mathbf{A} \mathbf{c} $$

</div>

<div class="column fragment" data-fragment-index="1">
<i class='fas fa-arrow-right'></i>
</div>

<div class="col-3 fragment" data-fragment-index="1">

$$ \mathbf{d} = \sum\limits_{k=1}^K \mathbf{A}_k \mathbf{c}_k $$

</div>

</div>

---

## Fuentes equivalentes <br> potenciadas por gradiente

---

<div class="r-stack">

<div class="fragment fade-out" data-fragment-index="0" style="width: 100%">
<p>Datos observados</p>
<img src="./images/equivalent-sources/eql-gradient-boosted-step0.svg"
style="width: 60%">
</div>

<div class="fragment current-visible" data-fragment-index="0" style="width: 100%">
<p>Defino fuentes</p>
<img src="./images/equivalent-sources/eql-gradient-boosted-step1.svg"
style="width: 60%">
</div>

</div>

---

#### Ventanas solapadas

<div class="r-stack">

<img class="fragment fade-out" data-fragment-index="0" src="./images/equivalent-sources/gradient-boosting-blocks/blocks0.svg" style="width: 30%">
<img class="fragment current-visible" data-fragment-index="0" src="./images/equivalent-sources/gradient-boosting-blocks/blocks1.svg" style="width: 30%">
<img class="fragment current-visible" src="./images/equivalent-sources/gradient-boosting-blocks/blocks2.svg" style="width: 30%">
<img class="fragment current-visible" src="./images/equivalent-sources/gradient-boosting-blocks/blocks3.svg" style="width: 30%">
<img class="fragment current-visible" src="./images/equivalent-sources/gradient-boosting-blocks/blocks4.svg" style="width: 30%">
<img class="fragment current-visible" src="./images/equivalent-sources/gradient-boosting-blocks/blocks5.svg" style="width: 30%">
<img class="fragment current-visible" src="./images/equivalent-sources/gradient-boosting-blocks/blocks6.svg" style="width: 30%">
<img class="fragment current-visible" src="./images/equivalent-sources/gradient-boosting-blocks/blocks7.svg" style="width: 30%">
<img class="fragment" src="./images/equivalent-sources/gradient-boosting-blocks/blocks8.svg" style="width: 30%">

</div>

---

### Ajustamos fuentes equivalentes iterativamente

---

<div class="r-stack">

<div class="fragment fade-out" data-fragment-index="0" style="width: 100%">
<p>Ajuste de <strong>fuentes</strong> de la primer ventana</p>
<img src="./images/equivalent-sources/eql-gradient-boosted-step2.svg"
style="width: 60%">
</div>

<div class="fragment current-visible" data-fragment-index="0" style="width: 100%">
<p>Cálculo del efecto de las <strong>fuentes</strong> y definición de
<strong>residuos</strong></p>
<img src="./images/equivalent-sources/eql-gradient-boosted-step3.svg"
style="width: 60%">
</div>

<div class="fragment current-visible" style="width: 100%">
<p>Ajuste de <strong>fuentes</strong> de la segunda ventana</p>
<img src="./images/equivalent-sources/eql-gradient-boosted-step4.svg"
style="width: 60%">
</div>

<div class="fragment" style="width: 100%">
<p>Cálculo del efecto de las <strong>fuentes</strong> y actualización de
<strong>residuos</strong></p>
<img src="./images/equivalent-sources/eql-gradient-boosted-step5.svg"
style="width: 60%">
</div>

</div>

---

### Repetimos para todas las ventanas

---

## Características

<ul>
<li class="fragment">Superposición de ventanas: <strong>autocorrección</strong></li>
<li class="fragment">Ajuste sobre <strong>datos en ventana</strong></li>
<li class="fragment"><strong>Predicciones libres</strong></li>
</ul>

---

# Ubicación de las fuentes

---

## Fuentes debajo de datos

<img src="./images/equivalent-sources/sources-below-data.svg" style="width: 60%">

<p class="fragment">
Posible anisotropía $\Rightarrow$ <strong>aliasing</strong>
</p>

---

## Fuentes en grilla regular

<img src="./images/equivalent-sources/grid-sources.svg" style="width: 60%">

<p class="fragment">
$M$ fuentes > $N$ datos $\Rightarrow$ problema <strong>subdeterminado</strong>
</p>

---

# Fuentes promediadas por bloque

---

<div class="r-stack">
<img class="fragment fade-out" data-fragment-index="0" src="./images/equivalent-sources/block-averaged-sources-0.svg" style="width: 60%">
<img class="fragment current-visible" data-fragment-index="0" src="./images/equivalent-sources/block-averaged-sources-1.svg" style="width: 60%">
<img class="fragment current-visible" src="./images/equivalent-sources/block-averaged-sources-2.svg" style="width: 60%">
<img class="fragment" src="./images/equivalent-sources/block-averaged-sources-3.svg" style="width: 60%">
</div>

---

## Características

<ul>
    <li>Evita <strong>anisotropías</strong></li>
    <li>$N$ datos > $M$ fuentes</li>
    <ul style="margin-left: 100px">
        <li>Problema <strong>sobredeterminado</strong></li>
        <li>Reduce uso de memoria</li>
    </ul>
    <li><strong>Tamaño de bloques</strong> controla <strong>cantidad de fuentes</strong></li>
</ul>

---

# Prueba con datos sintéticos

<img src="./images/equivalent-sources/synthetic-surveys.svg" style="width: 80%">

---

## Resultados

---

### Fuentes promediadas por bloque

<ul >
    <li class="fragment">Precisión equivalente</li>
    <li class="fragment">Menor cantidad de fuentes: reduce uso de memoria</li>
</ul>

---

### Fuentes equivalentes potenciadas por gradiente

<ul>
    <li class="fragment">Menor precisión</li>
    <li class="fragment">Menor tiempo de cómputo</li>
    <li class="fragment">
        <i class='fas fa-arrow-circle-up'></i> Tamaño de ventana
        <i class='fas fa-arrow-circle-up'></i> Precisión
    </li>
    <li class="fragment">Ventanas aleatorias: mejores predicciones</li>
</ul>

---

# Grillado de datos <br> gravimétricos de Australia

---

+1.7 millones de puntos

<div class="container" style="align-items: center;">
<div class="column">
<img src="./images/equivalent-sources/australia-data.jpg" style="width: 100%; height: auto;">
</div>
<div class="column">
<img src="./images/equivalent-sources/australia-data-zoom.jpg" style="width: 100%; height: auto;">
</div>
</div>


---

Grillados con fuentes equivalentes potenciadas con gradiente

<div class="container" style="align-items: center;">
<div class="column">
<img src="./images/equivalent-sources/australia-grid.jpg" style="width: 100%; height: auto;">
</div>
<div class="column">
<img src="./images/equivalent-sources/australia-grid-zoom.jpg" style="width: 100%; height: auto;">
</div>
</div>


---

<!-- .slide: data-background-color="#2b2b2b" -->

# Fatiando a Terra

---

## Complejización del problema científico

---

<div class="r-stack">
<img class="fragment fade-out" data-fragment-index="0" src="./images/fatiando/scientific-problem-step0.svg" style="width: 70%">
<img class="fragment" data-fragment-index="0" src="./images/fatiando/scientific-problem.svg" style="width: 70%">
</div>


<div class="footnote">

Figura modificada de
[Open Source](https://storage.googleapis.com/simpeg/lapis2019/9-open-source.pdf)
por D. Oldenburg, S. Kang & L. Heagy ([GeoSci.xyz](https://geosci.xyz/))
bajo [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

</div>

---

<!-- .slide: data-auto-animate -->

## Soluciones comunitarias

<img src="./images/fatiando/users-solid.svg" style="width: 20%">

---

<!-- .slide: data-auto-animate -->

## Soluciones comunitarias

<div class="container container-70">
<div class="column">
<img src="./images/fatiando/users-solid.svg" style="width: 60%">
</div>
<div class="column">
<img src="./images/fatiando/open-source.svg" style="width: 40%">
</div>
</div>

---

<!-- .slide: data-background-image="images/fatiando/fatiando-background.svg" -->

<a href="https://www.fatiando.org">
<img src="./images/fatiando/fatiando-banner.svg" alt="">
</a>

<p style="color: #f9f9f9; font-size: 2rem;">
En portugués significa <emph>cortando la Tierra</emph>
</p>

---

<div class="container container-70">

<div class="column">
<img src="./images/fatiando/pooch-logo.svg" width="80%">
<p class="small-font">
    <strong>Descarga y almacena</strong> <br> datos científicos
</p>
<ul class="fa-ul project-icons">
<li><i class="fa-li fab fa-github fa-fw" title="Github repository"></i>
   <a href="https://github.com/fatiando/pooch">fatiando/pooch</a>
</li>
<li><i class="fa-li fas fa-bookmark fa-fw" title="Publication"></i>
   doi: <a href="https://doi.org/10.21105/joss.01943">10.21105/joss.01943</a>
</li>
</ul>
</div>

<div class="column">
<img src="./images/fatiando/verde-logo.svg" width="80%">
<p class="small-font">
    Procesado y <strong>grillado</strong> <br>
    de datos espaciales
</p>
<ul class="fa-ul project-icons">
<li><i class="fa-li fab fa-github fa-fw" title="Github repository"></i>
   <a href="https://github.com/fatiando/verde">fatiando/verde</a>
</li>
<li><i class="fa-li fas fa-bookmark fa-fw" title="Publication"></i>
   doi: <a href="https://doi.org/10.21105/joss.00957">10.21105/joss.00957</a>
</li>
</ul>
</div>

</div>

<div class="container container-70" style="margin-top: 10rem;">

<div class="column">
<img src="./images/fatiando/boule-logo.svg" width="80%">
<p class="small-font">
    <strong>Elipsoide de referencia</strong> y <br>
    <strong>gravedad normal</strong>
</p>
<ul class="fa-ul project-icons">
<li><i class="fa-li fab fa-github fa-fw" title="Github repository"></i>
   <a href="https://github.com/fatiando/boule">fatiando/boule</a>
</li>
</ul>
</div>

<div class="column">
<img src="./images/fatiando/harmonica-logo.svg" width="80%">
<p class="small-font"> Procesado y modelado de datos <strong>gravimétricos y magnéticos</strong></p>
<ul class="fa-ul project-icons">
<li><i class="fa-li fab fa-github fa-fw" title="Github repository"></i>
   <a href="https://github.com/fatiando/harmonica">fatiando/harmonica</a>
</li>
</ul>
</div>

</div>

---

<img src="./images/fatiando/harmonica-logo.svg" width="60%">

- Teseroides de densidad variable
- Fuentes equivalentes potenciadas por gradiente

---

### Teseroides de densidad variable

<div class="container container-80">

<pre style="height: 35rem"><code data-trim data-noescape>
import boule as bl
import harmonica as hm

radio_medio = bl.WGS84.mean_radius

teseroide = [-70, -60, -40, -30, radio_medio - 10e3, radio_medio]

# Definimos una densidad lineal para este teseroide.
@njit
def densidad_lineal(radio):
    """Funcion de densidad lineal"""
    return a * radio + b

gravedad = hm.tesseroid_gravity(
    coordenadas, teseroide, densidad_lineal, field="g_z"
)
</code></pre>

</div>


---

### Fuentes equivalentes potenciadas por gradiente

<div class="container container-80">

<pre style="height: 26rem;"><code data-trim data-noescape class="python hljs">
import harmonica as hm

fuentes_eq = hm.EquivalentSourcesGB(
    depth=9e3,
    damping=10,
    window_size=100e3,
    block_size=2e3,
)

fuentes_eq.fit(coordenadas, datos)

grilla = fuentes_eq.grid(upward=1e3, spacing=2e3)
</code></pre>

</div>


---

## Mejores prácticas

- Documentación
- Pruebas de software
- Revisión por pares

---

## Retroalimentación

<img src="./images/fatiando/science-oss-feedback.svg" style="width: 35%">

---

## ¿Quiénes lo usan?

---

<div class="r-stack">
<img class="fragment fade-out" data-fragment-index="0" src="images/fatiando/users_map.svg" style="width: 80%; height: auto">
<img class="fragment" data-fragment-index="0" src="images/fatiando/users_history.svg" style="width: 60%; height: auto">
</div>

---

## Ecosistema open-source en Geociencias

- simpeg
- gempy
- obspy

---

<!-- .slide: data-background-color="#2b2b2b" -->

# Conclusiones

---

## Teseroides con densidad variable

- Metodología de modelado directo
- Función de densidad arbitrarias
- Parámetros $D$ y $\delta$: errores <span>&#60;</span>  1%.
- Aplicación: modelado directo de la cuenca Neuquina

---

## Fuentes equivalentes potenciadas por gradiente

- Metodología para interpolación de grandes cantidades de datos
- Disminuye significativamente uso de memoria
- Alcanza mejores tiempos de cómputo
- Fuentes promediadas por bloque:
    - Previenen anisotropías
    - Requieren menor uso de memoria
- Aplicación: grillado de +1.7M de datos sobre Australia

---

## Software

- Fatiando a Terra: proyecto open-source para geofísica
- Implementaciones de las nuevas metodologías
- Mejores prácticas: alta calidad
- Retroalimentación con investigaciones científicas
- Integración ecosistema open-source en Geociencias

---



---

<!-- .slide: class="slide-title" -->

# Muchas gracias
