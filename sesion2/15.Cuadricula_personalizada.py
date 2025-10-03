import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

fig, ax = plt.subplots()
ax.plot(x, y, color="darkred", linewidth=3)

ax.minorticks_on()
ax.grid(True, which="major", linestyle="--", color="gray")
ax.grid(True, which="minor", linestyle=":", color="lightgray")

ax.set_title("Grafico con dos grillas")
ax.set_xlabel("Eje x")
ax.set_ylabel("Eje y")

plt.grid(True)
plt.show()




