num = int(input("Ingresa un número entero:\n"))
match num:
    case num if num > 0:
        print(f"El numero {num} es un numero positivo")
    case num if num < 0:
        print(f"El numero {num} es un numero negativo")
    case _:
        print("El numero que ingresaste es cero")