import matplotlib.pyplot as plt
import numpy as np

talleres = ["Robotica","Quimica","Diseño","Cocina"]
grupo_A = [21, 19, 24, 23]
grupo_B = [24, 23, 29, 27]
grupo_C = [22, 25, 21, 26]

x = np.arange(len(talleres))
ancho = 0.25

fig, ax = plt.subplots()
barra_A = ax.bar(x - ancho, grupo_A, width=ancho, label="Grupo A", color="#d92c18")
barra_B = ax.bar(x, grupo_B, width=ancho, label="Grupo B", color="#d9bc18")
barra_C = ax.bar(x + ancho, grupo_C, width=ancho, label="Grupo C", color="#4dd918")

for i in [barra_A, barra_B, barra_C]:
    for barra in i:
        altura = barra.get_height()
        ax.text(barra.get_x() + barra.get_width()/2, altura + 0.5, f"{altura}", fontsize=8, ha="center", va="bottom")

ax.set_title(" Asistencia a talleres")
ax.set_xlabel("talleres")
ax.set_ylabel("Grupos")
ax.set_xticks(x)
ax.set_xticklabels(talleres)
ax.legend()

promedio_total = np.mean(grupo_A + grupo_B + grupo_C)
ax.axhline(promedio_total, color="gray", linestyle="--", linewidth=1)
ax.text(len(talleres) - 0.5, promedio_total + 0.5, f"Promedio: {promedio_total:.1f}", fontsize=8)

plt.grid(True, axis="y", alpha=0.4, linestyle=":")
plt.tight_layout()
plt.show()
