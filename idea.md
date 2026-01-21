# Idées
Source : [Article court sur l'évacuation d'une salle](https://informatique-python.readthedocs.io/fr/latest/Projets/projets.html#evacuation-d-une-salle-deplacement-d-une-foule-dans-une-rue)

# Modèle physique proposé
$$v=\left(\begin{array}{c}
v_{0}\\
0
\end{array}\right)+F\left(d_{x},d_{y},t\right)$$

$$F:\left(d_{x},d_{y},t\right)\longmapsto\left(\begin{array}{c}
-\mathrm{sign}\left(d_{x}\right)v_{0}\exp\left(\frac{-d_{x}}{d_{0}}\right)\\
-\mathrm{sign}\left(d_{y}\right)v_{0}\exp\left(\frac{-d_{y}}{d_{0}}\right)
\end{array}\right)$$