import matplotlib.pyplot as plt
import barcode
from barcode.writer import ImageWriter
from PIL import Image
import qrcode



# ========== Código de Barras ==========
codigo = barcode.Code128("1234567890", writer=ImageWriter())
barcode_filename = codigo.save("codigo_barras")
print("✅ Código de barras guardado:", barcode_filename)

# ========== Código QR ==========
qr_data = "https://tuweb.com"
qr_img = qrcode.make(qr_data)
qr_img.save("codigo_qr.png")
print("✅ Código QR guardado como: codigo_qr.png")


# ========== Matplotlib ==========
plt.plot([0, 1, 2], [0, 1, 2])
plt.title("Gráfico de prueba")
plt.savefig("grafico.png")
plt.show()
