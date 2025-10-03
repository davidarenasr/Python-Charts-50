import matplotlib.pyplot as plt
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5])

suma = a + b
producto = a * b
division = a / b

x = np.arange(len(a))

plt.plot(x, suma, label="sumatoria (a + b)", marker="x")
plt.plot(x, producto, label="sumatoria (a + b)", marker="o")
plt.plot(x, division, label="sumatoria (a + b)", marker="D")

plt.xticks( x, [f"a={i}, b={j}" for i, j in zip(a , b)])
plt.xlabel("Indice / pares (a + b)")
plt.ylabel("Resultados")
plt.title("Operacion vectorizadas con numpy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


