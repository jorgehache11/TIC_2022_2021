def contador_letras_2():
    palabra=raw_input("Dime una palabra: ")
    vocales=0
    consonantes=0
    cont=0
    while(cont<len(palabra)):
        if(palabra[cont] in "aeiou"):
            vocales=vocales+1
        else:
            consonantes=consonantes+1
        cont=cont+1
    print("Numero de vocales: "+str(vocales))
    print("Numero de consonantes: "+str(consonantes))
    print("Numero de letras: "+str(vocales+consonantes))
    
contador_letras_2()

