from random import *

continuar = 's'
juegos_totales = 0
intento = 1


while continuar == 's' or continuar == 'S':
    nombre = input("Ingrese su nombre: ")

    print(f"Bienvenido {nombre} este juego tiene como objetivo de adivinar un numero entre el 1 y el 100")
    print("Solo cuentas con 8 intentos, suerte!")

    numero_aleatorio = randint(1,100)

    while True:
        win = int(input(f"Introduzca su {intento} intento: "))
        intento += 1

        if win == numero_aleatorio:
            print(f"¡Felicidades has ganado usando {intento} intentos!")
            break
        elif win < 1 or win > 100:
            print("Tu numero esta fuera del rango")
        elif win < numero_aleatorio:
            print("Tu numero que elegiste es menor al numero ganador")
        elif win > numero_aleatorio:
            print("Tu numero que elegiste es mayor al numero ganador")

        if intento > 8:
            print("LLegaste a tu limite de 8 intentos y por lo tanto perdiste!")
            break

    continuar = input("Desea continuar? (s/n):")
    intento = 0

    juegos_totales += 1
else:
    print("Juego terminado")
    print(f"Usted a jugado {juegos_totales} veces")