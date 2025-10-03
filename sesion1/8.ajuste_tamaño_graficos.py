import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10, 20, 45, 50, 60]


plt.figure(figsize=(8,4))
plt.plot(x, y, marker="s")

plt.title("grafico con tamaño ajustado")
plt.xlabel("tiempo")
plt.ylabel("velocidad")

plt.show()