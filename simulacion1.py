# Importo librerias necesarias
import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Creo un array vacio para agregarle numeros del 1 al 6
dado_uno = []
dado_dos = []
suma = []
# Itero 10 veces, seria como tirar un dado 10 vecees
for i in range(10000):
    # Agrego cada "tirada" en un array
    dado_uno.append(random.randrange(1, 7, 1))
    dado_dos.append(random.randrange(1, 7, 1))
# Imprimo los valores obtenidos para luego corroborar el grafico
# print(dado_uno)
# print(dado_dos)
# Sumo los valores obtenidos de los dos dados en un nuevo array o vector
suma = np.add(dado_uno, dado_dos)
# print(suma)
sns.distplot(suma, kde=False)
plt.title("Histograma")
plt.xlabel("Valores de la suma")
plt.ylabel("Frecuencia en 10000 iteraciones")
plt.show()


