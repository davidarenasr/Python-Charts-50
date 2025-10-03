import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 200)
y1 = x 
y2 = x ** 2
y3 = x ** 3

plt.plot(x, y1, color="purple", label="y = x", linewidth=2)
plt.plot(x, y2, color="red", label="y = x²", linewidth=2)
plt.plot(x, y3, color="green", label="y = x³", linewidth=2)

plt.title("Comparacion de funciones, lineal, cuadrada y cubica")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.axhline(0, color="gray", linestyle="--")
plt.axvline(0, color="gray", linestyle="--")
plt.legend()
plt.tight_layout()
plt.grid(True, alpha=0.2)
plt.show()
