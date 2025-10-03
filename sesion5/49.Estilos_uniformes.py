import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.style.use("seaborn-v0_8-darkgrid")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

ax1.plot(x, y1, color="blue", label=("Seno"))
ax1.set_title("funcion seno")
ax1.legend()

ax2.plot(x, y2, color="Orange", label=("Coseno"))
ax2.set_title("Coseno seno")
ax2.legend()

plt.suptitle("Estilos uniformes de los graficos", fontsize=14)
plt.tight_layout(rect=[0,0,1, 0.95])
plt.show()











