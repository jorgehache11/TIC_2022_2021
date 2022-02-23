def devuelve_el_mayor(num1,num2):
    if(num1>num2):
        mayor=num1
    else:
        mayor=num2
    return(mayor)

def numero_mas_grande():
    num1=input("Dime un numero: ")
    num2=input("Dime otro numero: ")
    
    print(devuelve_el_mayor(num1,num2))
    
numero_mas_grande()
