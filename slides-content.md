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

# Introducción

---

<!-- .slide: data-background-color="#2b2b2b" -->

# Teseroides de densidad variable

---

## ¿Qué es un teseroide?

---

<img src="images/tesseroid-definition.svg" alt="Teseroide en un sistema de referencia con sus límites latitudinales, longitudinales y radiales" style="width: 50%" >

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

<div class="container" style="align-items: center; justify-content: center; width: 70%; margin: auto">

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
<img src="images/tesseroid-glq.svg" alt="Teseroide con cuatro masas puntuales en su interior, representando cómo la Cuadratura de Gauss-Legendre lo aproxima por ellas." style="width: 70%" >
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

<img src="images/tesseroid-computation-point.svg" alt="Teseroide y punto de
cómputo, con una recta a trazos que ilustra la distancia que los separa"
style="width: 40%;">

<i class='fas fa-arrow-circle-up'></i> Distancia a punto de cómputo
$ \Rightarrow $
<i class='fas fa-arrow-circle-up'></i> Precisión

---

## Discretización adaptativa

---

<div class="r-stack">
<img class="fragment fade-out" data-fragment-index="0" src="images/adaptive-discretization-step0.svg" alt="Teseroide y punto de cómputo" style="width: 40%;">
<img class="fragment current-visible" data-fragment-index="0" src="images/adaptive-discretization-step1.svg" alt="Teseroide subdividido en 4 teseroides por el algoritmo de discretización adaptativa" style="width: 40%;">
<img class="fragment" src="images/adaptive-discretization-step2.svg" alt="Teseroide subdividido en 7 teseroides por el algoritmo de discretización adaptativa" style="width: 40%;">
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
<img class="fragment fade-out" data-fragment-index="0" src="images/density-based-discretization-step0.svg" style="width: 60%;">
<img class="fragment current-visible" data-fragment-index="0" src="images/density-based-discretization-step1.svg" style="width: 60%;">
<img class="fragment current-visible" src="images/density-based-discretization-step2.svg" style="width: 60%;">
<img class="fragment current-visible" src="images/density-based-discretization-step3.svg" style="width: 60%;">
<img class="fragment current-visible" src="images/density-based-discretization-step4.svg" style="width: 60%;">
<img class="fragment current-visible" src="images/density-based-discretization-step5.svg" style="width: 60%;">
<img class="fragment" src="images/density-based-discretization-step6.svg" style="width: 60%;">
</div>

---

### Discretización adaptativa bidimensional

---

<div class="r-stack">
<img class="fragment fade-out" data-fragment-index="0" src="images/density-based-plus-adaptive-discret-step0.svg" style="width: 40%;">
<img class="fragment current-visible" data-fragment-index="0" src="images/density-based-plus-adaptive-discret-step1.svg" style="width: 40%;">
<img class="fragment current-visible" src="images/density-based-plus-adaptive-discret-step2.svg" style="width: 40%;">
<img class="fragment current-visible" src="images/density-based-plus-adaptive-discret-step3.svg" style="width: 40%;">
<img class="fragment" src="images/density-based-plus-adaptive-discret-step4.svg" style="width: 40%;">
</div>

---

### Cuadratura de Gauss-Legendre


<div class="container" style="align-items: center; justify-content: center; width: 70%; margin: auto">

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
<img src="images/tesseroid-small-glq.svg" style="width: 70%" >
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

<div class="container" style="align-items: center; justify-content: center; width: 70%; margin: auto">

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

<div class="container" style="justify-content: center; align-items: center;">

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

<img src="images/d-delta-grid-search.svg" style="width: 90%;">

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


<img src="./images/cuenca-neuquina-espesor.svg" style="width: 70%;">

---

## Campos gravitatorios del modelo


<img src="./images/cuenca-neuquina-resultados.svg" style="width: 70%;">

---

## Diferencias con densidad constante


<img src="./images/cuenca-neuquina-diff.svg" style="width: 70%;">

---

<!-- .slide: data-background-color="#2b2b2b" -->

# Fuentes equivalentes <br> potenciadas por gradiente

---

# Fatiando a Terra

---

# Conclusiones

---


# Math

$$  \color{#bf0101}{f(x)}  = \int\limits_{0}^{1} g(x) dx $$

---

# Regular slide

## With subtitles

---

# Do you want columns?

<div class="container">

<div class="column">
<img src="images/about.jpg" style="margin-top: 5%; border-radius: 50%; width: 80%;">
</div>

<div class="col-2">
<div class="centered">

* Licenciado en Física (UNR)
* Estudiante de Doctorado en Geofísica (UNSJ)
* Becario Doctoral de CONICET
* Desarrollador de [Fatiando a Terra](https://www.fatiando.org)
* Miembro de [Computer-Oriented Geoscience Lab](https://www.compgeolab.org)

</div>
</div>

</div>

---

# You can add fade-in animations

<div class="container">

<div class="column fragment fade-in">

First element

</div>

<div class="column fragment fade-in">

Second element

</div>

</div>

---

## Even on lists

<ul>
<li class="fragment fade-in">First element</li>
<li class="fragment fade-in">Second element</li>
<li class="fragment fade-in">Third element</li>
</ul>

---

## Highlight current item on list

<ol>
<li class="fragment highlight-current-red">First element</li>
<li class="fragment highlight-current-red">Second element</li>
<li class="fragment highlight-current-red">Third element</li>
</ol>

---

# You can put footnotes

<div class="bottom">

https://www.blog.pythonlibrary.org/2019/04/11/python-used-to-take-photo-of-black-hole/

</div>

---

<!-- .slide: data-background-color="#eceff4" -->

## You can change the background color

---

## Add quotes

<blockquote>
This is a quote
</blockquote>

---

## Add code

```python
import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 10, 11)

plt.plot(a, a ** 2)
plt.show()
```

---

# Contacto

<div>

<ul class="fa-ul">
<li><i class="fa-li fa fa-envelope"></i>

[santiago.r.soler@gmail.com](mailto:santiago.r.soler@gmail.com)

</li>
<li><i class="fa-li fab fa-twitter"></i>

[@santirsoler](https://twitter.com/santirsoler)

</li>
<li><i class="fa-li fa fa-globe-americas"></i>

[www.santisoler.com](https://www.santisoler.com)

</li>
</ul>

</div>

---

<!-- .slide: class="slide-license" -->

<p class="license-icons">
<i class="fab fa-creative-commons"></i><i class="fab fa-creative-commons-by"></i>
</p>

El contenido de esta presentación está disponible bajo <br>
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/)

---

<!-- .slide: class="slide-title" -->

# Muchas gracias
