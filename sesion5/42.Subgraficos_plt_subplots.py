import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10,4))

plt.subplot(1, 2, 1)
plt.plot(x, y1, color="blue")
plt.title("Seno")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x, y2, color="orange")
plt.title("Coseno")
plt.grid(True)

plt.suptitle("Grafico de Seno y Coseno")
plt.tight_layout()
plt.show()