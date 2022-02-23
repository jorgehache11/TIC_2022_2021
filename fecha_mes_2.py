def fecha_mes_2():
    fecha=raw_input("Introduce la fecha (dd/mm/aa): ")
    numero_mes=int(fecha[3])*10+int(fecha[4])
    nombres_meses="Enero,Febrero,Marzo,Abril,Mayo,Junio,Julio,Agosto,Septiembre,Octubre,Noviembre,Diciembre,"
    
    print(numero_mes)
    numero_comas=0
    cont=0
    mes=" "
    #Repasamos la cadena de los meses
    while(numero_comas<=numero_mes-1):
   #Vamos contando las comas
        if(nombres_meses[cont]==','):
            numero_comas=numero_comas+1
    #Cuando el número de comas es un nº menos que
#el número del mes que queremos, empezamos a formar 
#el nombre del mes
        if(numero_comas==numero_mes-1):
            if(nombres_meses[cont]!=','):
                mes=mes+nombres_meses[cont]


        #print("cont= "+str(cont)+" "+nombres_meses[cont]+" comas= "+str(numero_comas) )
        cont=cont+1
    #print("cont= "+str(cont))
    #print("comas= "+str(numero_comas))
    print("Estoy en el mes de"+mes)


   


fecha_mes_2()
