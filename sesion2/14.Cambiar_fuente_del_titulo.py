import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.plot(x, y, color="purple")
plt.title("Grafico con fuente personalizada", fontdict={
    "fontsize": 22,
    "fontweight": "bold",
    "color": "darkred"
})
plt.xlabel("Eje x", fontsize=12, color="blue")
plt.ylabel ("Eje y", fontsize=12, color="blue")
plt.grid(True)
plt.show()