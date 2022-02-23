def devuelve_el_mayor(num1,num2,num3):
    if(num1>num2 and num1>num3):
        mayor=num1
    else:
        if(num2>num1 and num2>num3):
            mayor=num2
        else:
            mayor=num3
    return(mayor)

def numero_mas_grande():
    num1=input("Dime un numero: ")
    num2=input("Dime otro numero: ")
    num3=input("Dime otro numero: ")
    print("El mayor es: "+str(devuelve_el_mayor(num1,num2,num3)))
    
numero_mas_grande()
