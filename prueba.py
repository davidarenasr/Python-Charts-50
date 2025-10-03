import matplotlib.pyplot as plt
import numpy as np

# Simulación de datos
dias = np.arange(1, 11)  # Arreglado: ahora hay 10 días
movimientos = np.array([5000, -500, -250, 3000, -7000, 1000, -1500, 2000, 10000, 1000])
saldo_inicial = 3000
saldo_diario = saldo_inicial + np.cumsum(movimientos)

# Colores para las barras
colores = ['green' if m >= 0 else 'red' for m in movimientos]

# Crear figura y ejes
fig, ax1 = plt.subplots(figsize=(12, 6))

# Gráfico de barras: ingresos/egresos
ax1.bar(dias, movimientos, color=colores, label="Movimientos diarios", alpha=0.7)
ax1.axhline(0, color="black", linestyle="--")
ax1.set_ylabel("Ingresos / Egresos ($)")
ax1.set_xlabel("Día")

# Segundo eje y: línea de saldo acumulado
ax2 = ax1.twinx()
ax2.plot(dias, saldo_diario, color="blue", marker="o", linewidth=2, label="Saldo acumulado", zorder=5)
ax2.set_ylabel("Saldo acumulado ($)")

# Títulos y leyendas
plt.title("Simulación financiera: ingresos, egresos y saldo")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.grid(True)
plt.tight_layout()
plt.show()
















