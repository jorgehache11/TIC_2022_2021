def contador_letras():
    palabra=raw_input("Dime una palabra: ")
    vocales=0
    consonantes=0
    cont=0
    while(cont<len(palabra)):
        if(palabra[cont]=='a'):
            vocales=vocales+1
        else:
            if(palabra[cont]=='e'):
                vocales=vocales+1
            else:
                if(palabra[cont]=='i'):
                    vocales=vocales+1
                else:
                    if(palabra[cont]=='o'):
                        vocales=vocales+1
                    else:
                        if(palabra[cont]=='u'):
                            vocales=vocales+1
                        else:
                            consonantes=consonantes+1
        cont=cont+1
    
    print("Numero de vocales: "+str(vocales))
    print("Numero de consonantes: "+str(consonantes))
    print("Numero de letras: "+str(vocales+consonantes))
    
contador_letras()
