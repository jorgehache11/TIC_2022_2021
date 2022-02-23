def nota_evau():
    print("CALCULADORA DE LA NOTA DE LA EVAU")
    print("")
    print("============= CARRERAS =============")
    carr1=raw_input("Primera opcion de carrera: ")
    carr2=raw_input("Segunda opcion de carrera: ")
    carr3=raw_input("Tercera opcion de carrera: ")
    print("====================================")
    print("")
    print("======== NOTAS DE ADMISION =========")
    nota_carr1=input("Nota de admision de "+carr1+": ")
    nota_carr2=input("Nota de admision de "+carr2+": ")
    nota_carr3=input("Nota de admision de "+carr3+": ")
    print("====================================")
    nota_media_1=0
    print("")
    print("========= FASE OBLIGATORIA =========")
    n1=float(input("Nota de Historia en la EVAU: "))
    n2=float(input("Nota de Lengua en la EVAU: "))
    n3=float(input("Nota de Ingles en la EVAU: "))
    n4=float(input("Nota de Matematicas en la EVAU: "))
    print("====================================")
    nota_media_1=((n1+n2+n3+n4)/4.0)

    if(nota_media_1<4):
        print("No has superado la fase obligatoria de la EVAU")
        print("")
        print("======= FASE EXTRAORDINARIA ========")
        n1=float(input("Nota de Historia en la EVAU: "))
        n2=float(input("Nota de Lengua en la EVAU: "))
        n3=float(input("Nota de Ingles en la EVAU: "))
        n4=float(input("Nota de Matematicas en la EVAU: "))
        print("====================================")
        print("")
        print("====== MEDIA DE BACHILLERATO =======")
        nota_media_2=0
        bach=float(input("Introduce la media de bachillerato: "))
        print("====================================")
        print("")
        nota_media_2=(nota_media_1*0.4)+(bach*0.6)
    else:
        nota_media_2=0
        print("")
        print("====== MEDIA DE BACHILLERATO =======")
        bach=float(input("Introduce la media de bachillerato: "))
        print("====================================")
        print("")
        nota_media_2=(nota_media_1*0.4)+(bach*0.6)
        
    if(nota_media_2<5):
        print("No has superado la fase de acceso")
    else:
        nota_media_3=0
        print("========= FASE VOLUNTARIA ==========")
        n5=float(input("Nota de la primera optativa en la EVAU: "))
        n6=float(input("Nota de la segunda optativa en la EVAU: "))
        ponderacion1=input("Cuanto pondera la primera optativa(0/0.1/0.15/0.2): ")
        ponderacion2=input("Cuanto pondera la segunda optativa(0/0.1/0.15/0.2): ")
        print("====================================")
        print("")
        if(n5>=5 and n6>=5):
            nota_media_3=nota_media_2+(n5*ponderacion1)+(n6*ponderacion2)
        else:
            if(n5<5 and n6>=5):
                nota_media_3=nota_media_2+(n6*ponderacion2)
            else:
                if(n5>=5 and n6<5):
                    nota_media_3=nota_media_2+(n5*ponderacion1)
                else:
                    nota_media_3=nota_media_2

    print("LA NOTA DE LA FASE OBLIGATORIA: "+str(nota_media_1))
    
    print("LA NOTA DE ACCESO: "+str(nota_media_2))

    print("LA NOTA DE ADMISION: "+str(nota_media_3))

    if(nota_media_3>=nota_carr1):
        print("Podrias entrar en "+carr1)
    else:
        print("No podrias entrar en "+carr1)

    if(nota_media_3>=nota_carr2):
        print("Podrias entrar en "+carr2)
    else:
        print("No podrias entrar en "+carr2)

    if(nota_media_3>=nota_carr3):
        print("Podrias entrar en "+carr1)
    else:
        print("No podrias entrar en "+carr3)

    print("Mucho animo!!!")
    print("Programado por Jorge Hernandez Aznar")
nota_evau()
