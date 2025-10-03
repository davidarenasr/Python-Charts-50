import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)

plt.style.use("dark_background")

plt.plot(x, y, label="grafico con _mpl", color="red")
plt.title("Grafico prediseñado")
plt.xlabel("X")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.show()





# _mpl-gallery-nogrid    bmh    grayscale   ggplot    dark_background