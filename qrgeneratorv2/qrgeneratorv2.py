#entraste aqui para ver cual era el error?, no hay errores simplemente lo hice asi.
#para que lo arregles y que no seas vago !!!!
#no scriptkiddes, si programaodres 
#suerte <3 


import qrcode
import pyfiglet
import datetime
import time
import os

def praticar_mecanografia():
    palabras = ["python", "amor", "chocolate", "manteca", "perro", 
                "mamaguevo", "auto", "tijera", "cepillo"]
    
    lvl = 0
    intentos = 3
print("QR_GENERATOR es un script basado en crear QR")
print("eliga unas de esa palbras tinenes 3 intentos ")

for palabra in "palabras":
    
    print("\n palabras a escribir:")
    entra_user = input("Tu respuesta: ")
else:
    print(f"incorrecto. la palabra correcta era {palabra}")
intentos = 1

if intentos == 0:
    print("te quedaste sin intentos. fin del juego.")
breakpoint

print(f"\npuntacion final: {0} palbras correctas. ")

if __name__ == "__main__":
    praticar_mecanografia()

def efecto(mensaje, velocidad=0.05):
    for letra in mensaje:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
        print()
datos = datetime.datetime.now()
print("QR_GENERATOR V2!!!!")
date_generator = 1
print(date_generator)
recolector_date = True
print(recolector_date)
color_number1 = "red"
print(color_number1)
color_number2 = "blue"
print(color_number2)

print(pyfiglet.figlet_format("QR _ GENERATOR V2"))

texto = input("ingresa url o texto aqui: ")
nombre_archivo = ("qrv2.png")

if os.path.exists(nombre_archivo):
    os.remove(nombre_archivo)
    print(f"la imagen que existe {nombre_archivo} a sido borrado")
    
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("texto")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="blue")
img.save(nombre_archivo)


print(f"el codigo qr fue guardado con exito se guardo como {nombre_archivo} .")

while True:
    print(qr.add_data)
    time.sleep(4)
    print(" \n EL QR SE GENERO CON EXITO :" + "(ctrl + c) para salir")

print("\n-----Creditos-----")
print("Creado por: h4Ghosty")
print("version: 3.0")
print("Fecha de creacion: 2023")

efecto("F-E-L-I-Z N-A-V-I-D-A-D", speed=0.1)