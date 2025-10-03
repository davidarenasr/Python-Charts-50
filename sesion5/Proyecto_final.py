import matplotlib.pyplot as plt
import numpy as np

dias = np.arange(1,11)
movimientos = np.array([5000, -1500, -1000, -800, 2000, -300, -300, -800, -300, 500])
saldo_inicial = 3000
saldo_acumulado = saldo_inicial + np.cumsum(movimientos)

colores = ["green" if m >= 0 else "red" for m in movimientos]

fig, ax1 = plt.subplots(figsize=(12,6))

ax1.bar(dias, movimientos, color=colores, label="Ingresos / egresos", alpha=0.7)
ax1.axhline(0, color="black", linestyle="--")
ax1.set_xlabel("Dia")
ax1.set_ylabel("Ingresos / egresos ($)")

ax2 = ax1.twinx()
ax2.plot(dias, saldo_acumulado, color="blue", linewidth=2, marker="o", zorder=5)
ax2.set_ylabel("Saldo acumulado")

plt.title("Grafico financiero ingrsos/ egresos ($)")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.grid(True)
plt.show()



