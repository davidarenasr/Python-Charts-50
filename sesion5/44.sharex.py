import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = 3 * np.sin(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 6), sharex=True)

ax1.plot(x, y1, color="purple")
ax1.set_title("Seno Normal")
ax1.grid(True)

ax2.plot(x, y2, color="orange")
ax2.set_title("Seno escalado (2x)")
ax2.grid(True)

plt.suptitle("Comparacion de seno normal y seno escalado (2x)")
plt.tight_layout()
plt.show()