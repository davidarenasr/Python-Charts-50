import matplotlib.pyplot as plt
import numpy as np

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
ventas = [150, 200, 130, 180, 230]
temperatura = [25, 23, 29, 22, 21]
x = np.linspace(0, 10, 100)
y = np.sin(x)
valores = np.random.normal(loc=50, scale=10, size=200)

fig, axs = plt.subplots(2,2, figsize=(12,4))

axs[0,0].plot(dias, ventas, color="skyblue")
axs[0,0].set_title("Ventas semanales") 
axs[0,0].set_xlabel("Dias")
axs[0,0].set_ylabel("Ventas")
axs[0,0].grid(True)

axs[0,1].plot(dias, temperatura, color="purple")
axs[0,1].set_title("Promedio de temperatura semanal") 
axs[0,1].set_xlabel("Dias")
axs[0,1].set_ylabel("Temperatura")
axs[0,1].grid(True)

axs[1,0].plot(x, y, color="orange")
axs[1,0].set_title("Seno") 
axs[1,0].grid(True)

axs[1,1].hist(valores, bins=15, color="gray", alpha=0.8)
axs[1,1].set_title("Histograma aleatorio") 
axs[1,1].grid(True)

plt.suptitle("Dahsboar de comparacion de datos", fontsize=14 )
plt.subplots_adjust(top=1)
plt.tight_layout()
plt.show()
