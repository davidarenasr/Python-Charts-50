import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y  = x * 2

plt.plot(x, y, marker="o", color="blue")
plt.title("Introduccion a numpy y arrays")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.5)
plt.show()