import matplotlib.pyplot as pp

x = [1,2,3,4,5]
y = [3,6,9,12,15]

pp.plot(x, y, marker="s", color="blue", linestyle="-")

pp.title("Grafica con diferentes puntos")
pp.xlabel("Eje X")
pp.ylabel("Eje y")

pp.show()
