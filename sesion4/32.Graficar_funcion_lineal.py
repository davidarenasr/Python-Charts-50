import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,100)
y = 5 * x + 9

plt.plot(x, y, color="green")
plt.title("grafico lineal de la forma y = mx + 3")
plt.xlabel("X")
plt.ylabel("Y")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.grid(True, alpha=0.2)
plt.show()

