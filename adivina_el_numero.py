from random import *
nombre = input("Cómo te llamas?: ")
print("He pensado un número entre el 1 y el 100 y tienes 8 intentos para adivinar")

intentos = 0
estimado = 0
numero_secreto = randint(0, 100)

while intentos < 8:
    estimado = int(input("Dime el numero!: "))
    intentos += 1
    if estimado not in range(1, 101):
        print(f"El número {estimado} no está permitido")
    elif estimado < numero_secreto:
        print(f"Respuesta incorrecta, el {estimado} elegido es menor al numero secreto")
    elif estimado > numero_secreto:
        print(f"Respuesta incorrecta, el {estimado} elegido es mayor al numero secreto")
    elif estimado == numero_secreto:
        print(f"{nombre} acertaste en el {intentos}º! El {estimado} es el número secreto")
        break
if estimado != numero_secreto:
    print(f"Se acabaron los intentos, el numero secreto era {numero_secreto}")
