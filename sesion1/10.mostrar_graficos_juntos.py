import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [2,4,6,12,11]
y2 = [1,4,5,24,35]

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(x, y1, color="Green")
plt.title ("Grafico que representa Y1")

plt.subplot(1,2,2)
plt.plot(x, y2, color="Blue")
plt.title("Grafico que representa Y2")

plt.tight_layout()
plt.show()
