import random

x = random.randint(1, 20)

print("Adivina el número entre 1 y 20")

correcto = False

while not correcto:
    numero = int(input("Escribe un número: "))
    if numero < x:
        print("Más alto")
    elif numero > x:
        print("Más bajo")
    else:
        print("¡Correcto! El número era", x)
        correcto = True
