def cuadrado():
    
    fila_completa=""
    num=input("Dame un numero, jefe: ")
    
    for fil in range (1,num+1):
        for col in range (1,num+1):
            
            fila_completa=fila_completa+"1"
        
        print fila_completa
        fila_completa=""

cuadrado()
