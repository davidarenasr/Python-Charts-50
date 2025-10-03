import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [2,3,5,7,11]
y2 = [1,4,9,16,25]

plt.plot(x, y1, color="#f6f607", label="Primos")
plt.plot(x, y2, color="#3e3e2a", label="Cuadrados")

plt.title("Colores personalizados")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)

plt.show()
