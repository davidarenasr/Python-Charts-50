import matplotlib.pyplot as plt
import numpy as np

semanas = ["S1","S2","S3","S4","S5"]
inscritos = [14, 17, 19, 26, 12]

x = list(range(len(semanas)))

fig, ax = plt.subplots()
ax.plot(x, inscritos, marker="o", linestyle="-", color="green", label="Inscritos")

for i in range (len(inscritos)):
    etiqueta = f"{inscritos[i]}"
    ax.text( x[i], inscritos[i] + 0.5, etiqueta, fontsize=9, ha="center")

ax.set_title("Numero de inscritos al curso")
ax.set_xlabel("Semanas", color="green")
ax.set_ylabel("Inscritos", color="green")
ax.set_xticks(x)
ax.set_xticklabels(semanas)
ax.legend()
ax.grid(True)
plt.show()

