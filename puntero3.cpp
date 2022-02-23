#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
	//RESERVA DINAMICA DE MEMORIA
	char aux[100];//RESERVO VARIABLE AUXILIAR PROVISIONAL
	int longitud;//DEFINO EL TAMANIO DE LA PALABRA
	printf("\nDime una palabra: ");//DIME LA PALABRA
	scanf("%s",aux); //LEO LA PALABRA
	longitud=strlen(aux);
	char *palabra;//PALABRA ES PUNTERO (UNA VARIABLE QUE CONTIENE UNA DIRECCIÓN DE MEMORIA DE ALGO QUE ES UNA LETRA)
	palabra=(char*) malloc(longitud*sizeof(char)); //MEMORY ALLOCATION
    strcpy(palabra,aux);
    printf("\nRESULTADO: ");
    printf("%s",palabra);
    
    return(0);
}

