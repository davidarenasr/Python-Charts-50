import matplotlib.pyplot as plt

categorias = ["Python", "Java", "C++", "JavaScript"]
valores = [90, 70, 65, 80]

plt.barh(categorias, valores, color="purple")

plt.title("grafico de barras horizontal")
plt.xlabel("categorias")
plt.ylabel("valores")

plt.show()