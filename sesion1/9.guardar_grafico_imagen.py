import matplotlib.pyplot as plt

etiquetas = ["Manzanas", "Peras", "Ciruelas", "Uvas"]
valores = [40,15,25,20]
colores = ["Purple", "Yellow", "Blue", "Green"]
explode = [0.1, 0, 0, 0]

plt.figure(figsize=(6,6))
plt.pie (
    valores,
    labels=etiquetas,
    colors=colores,
    explode=explode,
    startangle=90,
    autopct="%1.1f%%",

)

plt.title("Como guardar imagenes con calidad")
plt.axis("equal")
plt.savefig("manzana.png", dpi=300)

plt.show()
