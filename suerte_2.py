import random

def suerte_2():
    for cont in range(1,4):
        num=random.randint(1,6)
        print("Dado Nº"+str(cont)+" = "+str(num))


suerte_2()
