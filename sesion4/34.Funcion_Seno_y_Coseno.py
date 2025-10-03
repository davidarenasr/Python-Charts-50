import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4 * np.pi, 300)
y_seno = np.sin(x)
y_coseno = np.cos(x)

plt.plot(x, y_seno, color="purple", linewidth=2, label="seno")
plt.plot(x, y_coseno, color="orange", linestyle="--", linewidth=2, label="coseno")

plt.title("Grafica del seno y del coseno")
plt.xlabel("Eje X (radianes)")
plt.ylabel("funciones")
plt.axhline(0, color="gray", linewidth=1)
plt.legend()
plt.grid(True)
plt.show()

