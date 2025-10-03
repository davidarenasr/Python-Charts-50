import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

fig, ax = plt.subplots()
ax.plot(x, y, color="green", linewidth=4)
ax.set_title("Lineas de referencia")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")

ax.axhline(y=3, color="red", linestyle="--", label="Corte Y=3")
ax.axvline(x=4, color="blue", linestyle=":", label="Corte X=4")

ax.legend()
plt.grid(True)
plt.show()

