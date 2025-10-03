import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0,10,100)
y= np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, color="black", linewidth=2)

ax.fill_between(x, y, color="skyblue", alpha=0.5, label="Onda del seno")

ax.set_title("Sombra bajo la curva del seno")
ax.set_xlabel("Eje x")
ax.set_ylabel("Eje Y")
ax.legend()

plt.grid(True)
plt.show()

