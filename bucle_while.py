def bucle_while():
    suma=0
    continuar="S"
    while(continuar=="S"):
        num=input("Introduce un numero: ")
        suma=suma+num
        continuar=raw_input("Quieres leer un unmero mas?(S/N): ")
    print("SUMA: "+str(suma))
    
bucle_while()

