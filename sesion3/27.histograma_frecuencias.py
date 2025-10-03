import matplotlib.pyplot as plt

edades = [13,14,14,14,15,15,15,15,16,16,17,17,17,18,18,19]

fig, ax = plt.subplots()
ax.hist(edades, bins=7, color="mediumseagreen", edgecolor="black")


ax.set_title("Histograma de edades de curso grado 11")
ax.set_xlabel("Edades")
ax.set_ylabel("grupos")
plt.grid(True, axis="y")
plt.show()
