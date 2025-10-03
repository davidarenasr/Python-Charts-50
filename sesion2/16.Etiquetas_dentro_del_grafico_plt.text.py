import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

fig, ax = plt.subplots()
ax.plot(x, y, marker="o", color="black")

for i in range(len(x)):
    etiqueta = (f"{x[i]},{y[i]}")
    ax.text(x[i],y[i] + 0.3, etiqueta, ha="center", fontsize=9 )

ax.set_title("Etiqueta dentro del puntos del grafico")
ax.set_xlabel ("Eje X")
ax.set_ylabel ("Eje Y")

plt.grid(True)
plt.show()
