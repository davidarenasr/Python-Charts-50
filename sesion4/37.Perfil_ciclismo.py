import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

tiempo = np.array([0.00, 3.39, 7.40, 11.24, 15.17, 19.02, 22.54, 26.39, 30.23, 34.19])
altitud = np.array([2640, 2667, 2695, 2716, 2747, 2783, 2812, 2847, 2891, 2916])

dist_total = 5.54 #km
distancias = np.linspace(0, dist_total, len(tiempo)) #[0, 1, 2,3, 4,5, 6,7,8, 9]

velocidades = []
for i in range (len(tiempo) - 1):
    delta_d = distancias[i + 1] - distancias[i] 
    delta_t = (tiempo[i + 1] - tiempo[i])/60
    v = delta_d / delta_t
    velocidades.append(v)

tiempo_suave = np.linspace(tiempo.min(), tiempo.max(), 300)
spline = make_interp_spline(tiempo, altitud)
altitud_suave = spline(tiempo_suave)

plt.figure(figsize=(12,6))
plt.plot(tiempo_suave, altitud_suave, color="green", label="Curva Suave")
plt.plot(tiempo, altitud, "o", color="black", label="Distancias reales" )

for i  in range (len(velocidades)):
    min_time = (tiempo[i] + tiempo[i + 1])/2 
    max_alt = (altitud[i] + altitud[i + 1])/2
    plt.text(min_time, max_alt + 10, f"{velocidades[i]:.1f} km/h", fontsize=8, ha="center", color="blue")

plt.title("Grafico de altitud con velocidad promedio en km/h")
plt.xlabel("tiempo(min)")
plt.ylabel("altitud(msnm)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# tiempo = 0.00, 3.39, 7.40, 11.24, 15.17, 19.02, 22.54, 26.39, 30.23, 34.19
# altitud = 2640, 2667, 2695, 2716, 2747, 2783, 2812, 2847, 2891, 2916
# distancia = 5.54 km

