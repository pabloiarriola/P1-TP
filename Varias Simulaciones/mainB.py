'''
¿Fue anómalo el 2015?
1990 y 2015 presentaron a la mayoría de los no-hitters de cualquier temporada de béisbol (hubo siete).
Dado que hay en promedio 251/115 no-hitters por temporada, ¿cuál es la probabilidad de tener siete o más en una temporada?


Instrucciones
-Dibuje 10000 muestras de una distribución de Poisson con una media de 251/115 
-Determinar cuántas de sus muestras tuvieron un resultado mayor o igual a 7
-Número de muestras (10000).

'''
import numpy as np

# Seed random number generator
np.random.seed(42)

# Draw 10,000 samples out of Poisson distribution: n_nohitters
n_nohitters = np.random.poisson((251 / 115), size=10000)

# Compute number of samples that are seven or greater: n_large
n_large = np.sum(n_nohitters >= 7)

# Compute probability of getting seven or more: p_large
p_large = n_large / 10000

# Print the result
print('Probability of seven or more no-hitters:', p_large)

