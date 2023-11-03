#Autores: Mariana David - Pablo Escobar
#Redes - Laboratorio 8
#Ejercicio 2.2.2- Imagen


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import numpy as np

# Cargar la imagen en formato RGBA
original_image = Image.open('input/tux.bmp')
original_image = original_image.convert("RGBA")

# Convertir la imagen en bytes y aplicar reshape
image_bytes = np.array(original_image).tobytes()
image_bytes = np.frombuffer(image_bytes, dtype=np.uint8).reshape(480, 405, 4)

# Clave AES de 16 bytes
key = get_random_bytes(16)

# --------------------------------------------------------------------------------------
# Cifrado en modo CBC
# --------------------------------------------------------------------------------------
cipher_cbc = AES.new(key, AES.MODE_CBC)
iv = get_random_bytes(16)
ciphertext_cbc = iv + cipher_cbc.encrypt(image_bytes.tobytes())

# Crear una nueva imagen desde los bytes cifrados en modo CBC
ciphertext_image_cbc = Image.frombytes("RGBA", (405, 480), ciphertext_cbc)

# Guardar la imagen cifrada en modo CBC
ciphertext_image_cbc.save("output/ciphertext_cbc.png")

# --------------------------------------------------------------------------------------
# Cifrado en modo ECB
# --------------------------------------------------------------------------------------

cipher_ecb = AES.new(key, AES.MODE_ECB)
ciphertext_ecb = cipher_ecb.encrypt(image_bytes.tobytes())

# Crear una nueva imagen desde los bytes cifrados en modo ECB
ciphertext_image_ecb = Image.frombytes("RGBA", (405, 480), ciphertext_ecb)

# Guardar la imagen cifrada en modo ECB
ciphertext_image_ecb.save("output/ciphertext_ecb.png")
