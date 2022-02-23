def devuelve_el_mayor_2():
    mayor=input("Introduce un numero: ")
    for cont in range (1,10):
        num=input("Introduce otro numero: ")
        if(num>mayor):
            mayor=num
    print("El mayor es: "+str(mayor))
devuelve_el_mayor_2()
