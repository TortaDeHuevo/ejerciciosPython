counter = 0
while counter <= 100:
    counter+=10
    print(f"Counter: {counter}")
    print("somos la bomba")   #Estas lineas si se cumplen por que estan antes del continue
    if counter == 50:
        continue
    print("chile piquin") #Estas lineas no se cumplen despues del continue
else:
    print("El ciclo se ha terminado")
    