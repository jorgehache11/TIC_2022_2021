package MiCodigo;

public class ManejaNumeros {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int suma;
		int suma2;
		
		MiParejaNumeros objeto1;//Declaro el objeto
		objeto1= new MiParejaNumeros(5,8);//Instancio
		MiParejaNumeros objeto2;
		objeto2= new MiParejaNumeros(1,4);
		
		objeto1.setNum1(6);
		objeto1.setNum2(4);
		objeto2.setNum1(4);
		objeto2.setNum2(1);
		
		suma=objeto1.devuelveSuma();
		suma2=objeto2.devuelveSuma();
		
		System.out.println("La suma de la pareja uno vale: ");
		System.out.println(suma);
		System.out.println("\nLa suma de la pareja dos vale: ");
		System.out.println(suma2);	
	}

}
 