import matplotlib.pyplot as plt

etiquetas = ["Pera", "Manzana", "Cerezas", "Durazno"]
tamaño = [20, 30, 25, 25]
colors = ["Blue", "blue", "White", "Blue"]

plt.pie(tamaño, labels=etiquetas, colors=colors, autopct="%1.1f%%", startangle=90)

plt.title("Descripcion de frutas")
plt.axis("equal")

plt.savefig( "pacman.png", dpi=300)
plt.show()
