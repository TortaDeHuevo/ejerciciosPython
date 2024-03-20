num1 = float(input("Ingresa un número: "))
num2 = float(input("Ingresa otro número: "))
num3 = float(input("Ingresa un último número: "))

if (num1 > num2) and (num1 > num3):
    print(f"El número {num1} es el mayor de los 3 nùmeros.")
elif (num2 > num3) and (num2 > num1):
    print(f"El número {num2} es el mayor de los 3 nùmeros.")
else: 
    print(f"El número {num3} es el mayor de los 3 nùmeros.")
    