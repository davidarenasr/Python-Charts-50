import matplotlib.pyplot as plt
import numpy as np

cursos = ["Matematicas", "Ciencias", "LecturaCritica", "artes"]
aprobados = [35, 31, 37, 39]
reprobados = [5, 9, 3, 1]

x = np.arange(len(cursos))
ancho = 0.35

fig, ax = plt.subplots()
barra1 = ax.bar(x - ancho/2, aprobados, color="blue", width=ancho, label="Aprobados")
barra2 = ax.bar(x + ancho/2, reprobados, color="red", width=ancho, label="Reprobados")

ax.set_title("Alumnos aprobados vs reprobados")
ax.set_xlabel("Cursos")
ax.set_ylabel("alumnos")
ax.set_xticks(x)
ax.set_xticklabels(cursos)

plt.legend()
plt.grid(True, axis="y")
plt.show()