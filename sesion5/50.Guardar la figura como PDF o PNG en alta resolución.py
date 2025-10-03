import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(12,6))
plt.plot(x, y, color="orange", label="Seno(x)",linewidth=3)
plt.title("Grafico ejemplo para bajar en al resolucion pdf, y png")
plt.xlabel("numeros")
plt.ylabel("Seno(x)")
plt.grid(True)

plt.savefig("Grafico_seno.png", dpi=300)
plt.savefig("Grafico_seno.pdf", dpi=300)
plt.show()



