def cambia_vocales_3():
    palabra=raw_input("Dime una palabra: ")
    vocal=raw_input("Que vocal quieres poner: ")
    cont=0
    nueva_palabra=" "
    while(cont<len(palabra)):
        if(palabra[cont]=='a'):
            nueva_palabra=nueva_palabra+vocal
        else:
            if(palabra[cont]=='e'):
                nueva_palabra=nueva_palabra+vocal
            else:
                if(palabra[cont]=='i'):
                    nueva_palabra=nueva_palabra+vocal
                else:
                    if(palabra[cont]=='o'):
                        nueva_palabra=nueva_palabra+vocal
                    else:
                        if(palabra[cont]=='u'):
                            nueva_palabra=nueva_palabra+vocal
                        else:
                            nueva_palabra=nueva_palabra+palabra[cont]
        
        cont=cont+1
        
    print("Palabra transformada "+nueva_palabra)

cambia_vocales_3()
