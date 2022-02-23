#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
	//RESERVA DINAMICA DE MEMORIA
	char aux[10];//RESERVO VARIABLE AUXILIAR PROVISIONAL
	int longitud;//DEFINO EL TAMANO DE LA PALABRA
	char *lista[3];
	int cont;
	for(cont=1;cont<4;cont++){
		//1. Leo el nombre de un rey
		printf("\nDime el nombre del rey %d: ",cont);
		//2. Lo guardo en una variable auxiliar
		scanf("%s",aux); 
		//3. Cuento numero de letras
		longitud=strlen(aux);
		//4. Busco un hueco en la memoria de ese tamano y me apunto su dirreccion
		lista[cont]=(char *)malloc(longitud*sizeof(char));
		//5. Copio el nombre desde auxiliar hasta el hueco encontrado
		strcpy(lista[cont],aux);	
	
	}
	printf("\n LOS TRES REYES MAGOS SON: ");
	for(cont=1;cont<4;cont++){
		printf("\n %s",lista[cont]);
	
	}
    return(0);

}

