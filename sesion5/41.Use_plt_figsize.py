import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 200)
y = np.sin(x)

plt.figure(figsize=(10, 6)) # 8 pulgadas por 4 pulgadas.
plt.plot(x, y, label="seno de x", color="orange")
plt.title("Grafico de 8 x 4 pulgadas")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
plt.legend()
plt.show()
