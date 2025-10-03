import matplotlib.pyplot as plt
import numpy as np

product = ["pan", "leche", "cafe", "huevos"]
venta_enero = [800, 200, 550, 350]
venta_febrero = [820, 190, 150, 380]

x = np.arange(len(product))
ancho = 0.35

fig, ax = plt.subplots()
barra1 = ax.bar(x - ancho/2, venta_enero, width=ancho, color="skyblue", label="Enero")
barra2 = ax.bar(x + ancho/2, venta_febrero, width=ancho, color="orange", label="Febrero")

ax.set_title("Comparativo de ventas enero vs febrero")
ax.set_xlabel("Productos")
ax.set_ylabel("Unidades vendidas")
ax.set_xticks(x)
ax.set_xticklabels(product)

plt.legend()
plt.grid(True, axis="y")
plt.show()

#desarrollar actividad para el curso de python. 