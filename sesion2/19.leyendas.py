import matplotlib.pyplot as plt

categorias = ["A", "B", "C"]
grupo1 = [12, 15, 13]
grupo2 = [14, 18, 19]

x = range(len(categorias))

plt.bar(x, grupo1, width=0.4, label="Grupo 01", align="center")
plt.bar([i + 0.4 for i in x], grupo2, width=0.4, label="Grupo 02", align="center")



plt.title("Grafico de barras con legend")
plt.xlabel("Categorias")
plt.xlabel("Valores")

plt.legend()
plt.show()



