import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Inicializo array de cuantos empleados llegan en un determinado dia
empleados_dia = []
# Cantidad de dias que quiero simular
n = 10000
# Para obtener la cantidad de gente que asistiria en un dia con las probabilidades asignadas por el area de recursos
# se me ocurre utilizar obtener un numero aleatorio entre 0 y 100. Si se encuentra entre 0 y 0.1 asigno que ese dia fue
# una persona, entre 0.1 y 0.25 dos, entre 0.25 y 0.5 tres, entre 0.5 y 0.85 y entre 0.85 y 1 cinco. (entiendo que en
# esto consiste el metodo de la transformada inversa)

for i in range(n):
    r = random.randrange(0, 101, 1)
    if 0 <= r < 10:
        empleados_dia.append(1)
    elif 10 <= r < 25:
        empleados_dia.append(2)
    elif 25 <= r < 50:
        empleados_dia.append(3)
    elif 50 <= r < 85:
        empleados_dia.append(4)
    else:
        empleados_dia.append(5)

sns.distplot(empleados_dia, kde=False)
plt.xlabel("Empleados que asistieron por dia")
plt.ylabel("Cantidad de dias")
plt.title("Histograma de asistencia de empleados por dia")
plt.show()




