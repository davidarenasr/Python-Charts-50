import matplotlib.pyplot as plt

categorias = ["Aprobados","Reprobados","Pendientes"]
cantidad = [65,25,10]
colores = ["#0dedea","#0d21ed","#ed1b0d"]

plt.figure(figsize=(6,6))
plt.pie(cantidad, labels=categorias, colors=colores, autopct="%1.2f%%", shadow=True, startangle=90 )
plt.title("Grafico de porcentajes de reprobacion en un grado", color="blue")
plt.axis(True)
plt.show()


