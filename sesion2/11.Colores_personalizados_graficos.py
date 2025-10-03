import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [3,13,4,14,5,20]

fig, ax = plt.subplots()

fig.patch.set_facecolor("#000000")
ax.set_facecolor("#ea0707")

ax.plot(x, y, color="#000000")
plt.title("Grafico con dos colores", color="#ea0707")
plt.xlabel("Eje X", color="#ea0707")
plt.ylabel("Eje Y", color="#ea0707")
plt.grid(True)

plt.show()



