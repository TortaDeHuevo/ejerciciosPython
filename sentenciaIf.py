a = 5
if a == 2:
    print("Esto es un 2")
if a == 5:
    print("Esto es un 5")
    print("Pero tambien se cumple esta cadena de texto")
if a >= 5:
    print("Esto es una cadena de texto, Hola Mundo")
if a != 4:
    print("Hola Mundo")

num = int(input("Ingresa un número entero:\n"))
match num:
    case num if num % 2 == 0:
        print("El numero es par")
    case _:
        print("El numero es impar")