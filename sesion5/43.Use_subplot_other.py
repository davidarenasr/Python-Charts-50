import matplotlib.pyplot as plt
import numpy as np

x = np.linspace( 0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(x, y1, color="green")
ax1.set_title("Seno")
ax1.grid(True)

ax2.plot(x, y2, color="blue")
ax2.set_title("Coseno")
ax2.grid(True)

plt.suptitle("Grafico de seno y coseno")
plt.tight_layout()
plt.show()
