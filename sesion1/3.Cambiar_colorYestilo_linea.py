import matplotlib.pyplot as plt

x = [2,5,7,9,10]
y = [3,6,8,11,13]

plt.plot (x, y, color="red", linestyle="--", marker="o")

plt.title("Linea con color rojo y guiones")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()