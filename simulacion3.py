import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

n = 5
pallets = []
pallets_hora = np.zeros(n)
hora = np.zeros(n)
#arribos_hora = []

for i in range(n):
    pallets.append(np.random.poisson(2))
    hora[i] = i + 1
    if i == 0:
        pallets_hora[i] = pallets[i]
    else:
        pallets_hora[i] = pallets[i] + pallets_hora[i - 1]

print(pallets)
print(pallets_hora)

# Quiero graficar el array pallet_hora donde el eje y representa la cantidad total de pallets (pallets_hora) y el eje x
# las horas del 0 a 5, nose como hacerlo con sns.distplot asi que uso plt.bar
# sns.distplot(pallets_hora, kde=False) ---> No funciona y nose que esta graficando
# sns.distplot(pallets, kde=False) ----> Muestra la distribucion poisson de nuestra variable aleatoria

plt.bar(hora, height=pallets_hora)
plt.title("Pallets por hora en deposito")
plt.xlabel("Hora")
plt.ylabel("Pallets en deposito")
plt.show()

