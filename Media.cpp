#include <stdio.h>

int main() {

    
    float x[10];
    int cont;
    float suma=0;
    float media;
    /*for in range(1,10):
    cont++ = cont=cont+1
    while(cont<=10){
    ...
    cont++;
    }*/
    for(cont=0;cont<10;cont++){
    //num=input("Dame un numero: "):
        printf("Dame un numero: ");
        scanf("%f",&x[cont]);
    }
    for(cont=0;cont<10;cont++){
        printf("\nx[%d]=%.2f",cont,x[cont]);    
        suma+=x[cont];
    //suma=suma+x[cont];
    }
    media=suma/10;
    printf("\n LA MEDIA VALE: %.2f",media);
    //cuidado con el %3.2f
    
    return 0;
}
