import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

fig, ax = plt.subplots()
ax.plot(x, y, color="green", linewidth=10)

ax.set_title("Grosor de linea")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
plt.grid(True)
plt.show()


