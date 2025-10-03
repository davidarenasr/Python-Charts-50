import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].plot(x , y1, color="orange")
axs[0].set_title("Seno de X")
axs[0].set_xlabel("Eje X")
axs[0].set_ylabel("Eje Y")
axs[0].grid(True)

axs[1].plot(x , y2, color="green")
axs[1].set_title("Coseno de X")
axs[1].set_xlabel("Eje X")
axs[1].set_ylabel("Eje Y")
axs[1].grid(True)

plt.suptitle("Subgraficos de seno y coseno")
plt.tight_layout()
plt.show()