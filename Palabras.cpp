#include <stdio.h>

int main() {

    char letras[11];
    int cont;
    
    for(cont=1;cont<=10;cont++){
        printf("Introduce la letra %d: ",cont);
        scanf(" %c",&letras[cont]);
    }
    printf("\nHAS ESCRITO LA PALABRA:");
    for(cont=1;cont<=10;cont++){
        printf("%c",letras[cont]);    
    }
    
    return 0;
}

