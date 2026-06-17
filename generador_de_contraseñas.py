#enseñanza con claude
import random
import string
from pathlib import Path
from datetime import datetime

contraseñas_dir = Path("contraseñas.txt")
if not contraseñas_dir.exists():
    log = open("contraseñas.txt", "w")
    log.close()

while True:
    pregunta = input("quieres ver la lista de contraseñas? [si/no]: ")
    if pregunta == "no":
        break
    elif pregunta == "si":
        with open("contraseñas.txt", "r") as f:
            print(f.read())
        break
    else:
        print("respuesta no valida")

#Generador de contraseñas random.
def generar_constraseña():
    i = 0
    contraseña_random = ""
    nuevapool = string.digits + string.ascii_letters + string.punctuation

    while True:
        try:
            longitud = int(input("escribe la cantidad de caracteres que quieres para tu constraseña: "))
            break
        except ValueError:
            print("el numero asignado no es valido") 

    for i in range(longitud):
        contraseña_random = contraseña_random + random.choice(nuevapool)
       
    
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("contraseñas.txt", "a") as archivo:
        archivo.write(f"{fecha} | longitud: {longitud} | contraseña: {contraseña_random}\n")

    return f"\nLa contraseña generada es: {contraseña_random}"


print(generar_constraseña()) 

while True:
    generar_nuevo = input("\ndesea generar una contraseña diferente?: [si/no]: ")
    if generar_nuevo == "no":
        print("Hasta pronto!")
        break
    elif generar_nuevo == "si":
        print(generar_constraseña())
    else:
        print("respuesta no valida")
        
