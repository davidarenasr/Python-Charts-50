import matplotlib.pyplot as plt

horas_estudios=[1,2,3,4,5,6,7]
calificacion=[40,45,50,45,70,80,85]

plt.figure(figsize=(7,6))
plt.scatter(horas_estudios, calificacion, color="teal", marker="o", s=500)

plt.title("Grafico de dispersion simple")
plt.xlabel("horas de estudios")
plt.ylabel("calificaciones")
plt.grid(True)
plt.show()


