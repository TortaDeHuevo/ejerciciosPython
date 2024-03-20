import random
numero = random.randint(0,100)
print(numero)
suma = 0
for i in range(numero):
    if i%5 != 0 and i%7 != 0:
        suma += i
    print(suma)


'''
for n in range(numero+1):
    # Si no es múltiple de 5 y 7 lo sumamos
    if n % 5 != 0 and n % 7 != 0:
        sumatorio += n
'''