def cambia_vocales_2():
    palabra=raw_input("Dime una palabra: ")
    vocal=raw_input("Que vocal quieres poner: ")
    cont=0
    while(cont<len(palabra)):
        if(palabra[cont]=='a'):
            print (vocal)
        else:
            if(palabra[cont]=='e'):
                print (vocal)
            else:
                if(palabra[cont]=='i'):
                    print (vocal)
                else:
                    if(palabra[cont]=='o'):
                        print (vocal)
                    else:
                        if(palabra[cont]=='u'):
                            print (vocal)
                        else:
                            print (palabra[cont])
        cont=cont+1
    
    
    print("Palabra transformada "+palabra)
    
cambia_vocales_2()
