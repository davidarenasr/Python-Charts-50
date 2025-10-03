import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 25, 300)
y = np.sqrt(x)

plt.plot(x, y, color="blue", label="Raiz Cuadrada de X", linewidth=2)
plt.title("Grafico de raiz cuadrada", color="yellow")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.axhline(0, color="red", linestyle="--")
plt.legend()
plt.grid(True)
plt.show()

 