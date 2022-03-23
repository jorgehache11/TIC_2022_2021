package MiCodigo;

public class ManejaVehiculo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Vehiculo miBarquito;
		Coche miCoche;
		CocheElectrico miTesla;
		miBarquito=new Vehiculo("Titanic II","acuatico");
		miCoche=new Coche("Rayo McQueen","terrestre");
		miTesla=new CocheElectrico("Tesla","terrestre");
		System.out.println("Mi coche electrico es un "+miTesla.getIdentificador());
		System.out.println("Mi vehiculo el"+miCoche.getIdentificador()+" es un vehiculo "+miCoche.getMedio());
		System.out.println("Mi vehiculo el"+miBarquito.getIdentificador()+" es un vehiculo "+miBarquito.getMedio());
	}

}
