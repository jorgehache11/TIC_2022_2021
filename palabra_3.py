def palabra_3():
    nombre=raw_input("Nombre: ")
    apellido=raw_input("Apellido: ")
    print("Buenos dias, "+nombre+" "+apellido)
    print("Tu lindo nombre empieza por la letra "+nombre[0])
    print("Voy a deletrear tu nombre")
    for cont in range(0,20):
        print(nombre[cont])
    
palabra_3()
