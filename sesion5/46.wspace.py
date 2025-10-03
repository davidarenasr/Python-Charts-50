import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y3 = np.clip(y3, -10, 10)

fig, axs = plt.subplots(1, 3, figsize=(12,4))

axs[0].plot(x, y1, color="purple")
axs[0].set_title("Seno de X")
axs[0].grid(True)

axs[1].plot(x, y2, color="orange")
axs[1].set_title("Coseno de X")
axs[1].grid(True)

axs[2].plot(x, y3, color="blue")
axs[2].set_title("tangente X")
axs[2].grid(True)

plt.subplots_adjust(wspace=0.4, hspace=0.2)
plt.suptitle("Comparacion de graficos trigonometricos")
plt.show()