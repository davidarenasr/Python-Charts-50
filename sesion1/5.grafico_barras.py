import matplotlib.pyplot as plt

categorias = ["A", "B", "C", "D"]
valores = [12, 19, 8, 15]

plt.bar(categorias, valores, color="blue")

plt.title("grafico de barras")
plt.xlabel("categorias")
plt.ylabel("valores")

plt.show()