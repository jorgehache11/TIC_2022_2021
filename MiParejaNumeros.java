package MiCodigo;

public class MiParejaNumeros {
	
	//Atributos=Variables
	
	int num1;
	int num2;
	
	//Constructor
	
	public MiParejaNumeros(int num1,int num2){
		this.num1=num1;
		this.num2=num2;
	}
	
	//M�todos set/get
	
	void setNum1(int num1){
		this.num1=num1;
	}
	void setNum2(int num2) {
		this.num2=num2;
	}
	int getNum1() {
		return num1;
	}
	int getNum2() {
		return num2;
	}
	
	//M�todos=Funciones
	
	public int devuelveSuma() {
		return (num1+num2);
		
	}
	public int devuelveResta() {
		return (num1-num2);
		
	}
	public int devuelveMultiplicacion() {
		return (num1*num2);
		
	}
	public int devuelveDivision() { 
		return (num1/num2);
		
	}
	
}
