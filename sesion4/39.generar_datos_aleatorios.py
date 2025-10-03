import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

datos = np.random.normal(loc=0, scale=1, size=100)

plt.hist(datos, bins=15, color="skyblue", edgecolor="black")
plt.title("Histograma con datos aleatorios")
plt.xlabel("datos")
plt.ylabel("Agrupaciones")
plt.show()

