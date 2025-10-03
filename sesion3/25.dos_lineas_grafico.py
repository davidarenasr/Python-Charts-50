import matplotlib.pyplot as plt
import numpy as np

materias = ["Matematicas","Quimica","Fisica","Biologia","Ambiental"]
aprobados = [36,32,30,38,39]
reprobados = [4,8,10,2,1]

x = list(range(len(materias)))
fig,ax = plt.subplots()
ax.plot(x, aprobados, marker="o", linestyle="--", color="orange", label="Aprobados")
ax.plot(x, reprobados, marker="s", linestyle="-", color="green", label="reprobados" )


ax.set_title("Graficos lineales de comparacion")
ax.set_xlabel("Materias")
ax.set_ylabel("Estudiantes")
ax.set_xticks(x)
ax.set_xticklabels(materias)
ax.legend()
ax.grid(True)

plt.show()