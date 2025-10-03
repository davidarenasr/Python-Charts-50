import matplotlib.pyplot as plt

categorias = ["Producto_A","Producto_B","Producto_C","Producto_D"]
valores = [140, -60, 90, -30]
colores = ["green" if val >= 0 else "red" for val in valores]

fig, ax = plt.subplots()
barras = ax.bar(categorias, valores, color=colores)

for barra in barras:
    altura = barra.get_height()
    ax.text (barra.get_x() + barra.get_width()/2, altura + (3 if altura >= 0 else -3), 
             f"{altura}", ha="center", va="bottom" if altura >=0 else "top", fontsize=8, color="black" 
             )
    
ax.set_title("Ganancias y perdidas de ventas en productos")
ax.set_ylabel("Valores en USD")
ax.axhline(0, color="black", linewidth=1)

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

