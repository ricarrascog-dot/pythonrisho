from random import randint

num1 = int(input("Ingrese límite inferior: "))
num2 = int(input("Ingrese límite superior: "))

numero = randint(num1, num2)

7
if numero % 2 != 0:
    if numero + 1 <= num2:
        numero += 1
    else:
        numero -= 1

intentos = 3
prev_guess = None  

for i in range(intentos):
    guess = int(input("Intente adivinar: "))
    if guess == numero:
        print("Felicitaciones, pudiste adivinar.")
        break
    else:
        if i == 0:
            print("El número es mayor." if guess < numero else "El número es menor.")
        elif i == 1:
            print("El número es mayor." if guess < numero else "El número es menor.")
            print("Te daré una pista:")
            if abs(numero - guess) < abs(numero - prev_guess):
                print(f"El número que buscas está más cerca de {guess} que de {prev_guess}")
            else:
                print(f"El número que buscas está más cerca de {prev_guess} que de {guess}")
        elif i == 2:
            print("Perdiste.")
            print("El número era:", numero)
    prev_guess = guess