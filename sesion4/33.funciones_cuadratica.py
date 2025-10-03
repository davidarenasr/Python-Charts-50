import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 200)

a = 1
b = 0
c = 3

y = a * x ** 2 + b * x + c
# ax² + bx + c 

plt.plot(x, y, label=" y = x²", color="purple")
plt.title("Grafico de funcion cuadratica")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.axhline(0, color="gray", linestyle="--")
plt.axvline(0, color="gray", linestyle="--")
plt.legend()
plt.grid(True, alpha=0.5)
plt.show()





