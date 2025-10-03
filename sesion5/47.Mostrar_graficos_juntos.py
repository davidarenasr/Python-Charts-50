import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.plot([1,2,3,4,5],[7,12,15,18,25], color="blue", marker="o")
plt.title("Linea de crecimiento")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)

plt.subplot(2,2,2)
categorias = ["A","B","C","D"]
valores = [15,40,35,28]
plt.bar(categorias, valores, color="orange" )
plt.title("Grafico de barras")
plt.ylim(0, 50)

plt.subplot(2,2,3)
x = [1,2,5,7,9,4,6]
y = [7,5,3,7,8,9,4]
plt.scatter(x, y, color="skyblue")
plt.title("Diagrama de dispersion")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.subplot(2,2,4)
labels = ["peras","duraznos","manzanas","limones"]
porcentajes = [40,25,15,20]
plt.pie(porcentajes, labels=labels, autopct="%1.1f%%", colors=["red","yellow","blue","green"])
plt.title("Grafico circular")

plt.tight_layout()
plt.show()