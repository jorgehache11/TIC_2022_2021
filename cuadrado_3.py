def cuadrado_3():
    fila_completa=""
    num=input("Dame un numero, jefe: ")
    
    for fil in range (1,num+1):
        for col in range (1,num+1):
            
            if(fil % 2 ==1 and col % 2==0):
                fila_completa=fila_completa+"0"
            else:
                if(fil % 2==0 and col % 2==1):
                    fila_completa=fila_completa+"0"
                else:
                    fila_completa=fila_completa+"1"
        
        print fila_completa
        fila_completa=""
            
cuadrado_3()
