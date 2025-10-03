import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 200)
y = -x**2 + 4*x + 10

max_index = np.argmax(y)
min_index = np.argmin(y)

plt.plot(x, y, label="-x² + 4x + 10")
plt.scatter(x[max_index], y[max_index], color="red", label=f"maximo {x[max_index]:.2F},{y[max_index]:.2f}")
plt.scatter(x[min_index], y[min_index], color="green", label=f"minimo {x[min_index]:.2f},{y[min_index]:.2f}")
plt.legend()

plt.title("Buscando maximos y minimos en funcion cuadratica")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
