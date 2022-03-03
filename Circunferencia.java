package MiCodigo;

public class Circunferencia {
	//ATRIBUTOS
	private MiParejaNumeros centroCirculo;
	private double radio;
	//CONSTRUCTOR
	public Circunferencia(int coordX, int coordY, double radio) {
		super();
		centroCirculo=new MiParejaNumeros(coordX,coordY);
		this.radio = radio;
	}
	//METODOS SET GET
	public int getCoordX() {
		return centroCirculo.getNum1();
	}

	public void setCoordX(int coordX) {
		centroCirculo.setNum1(coordX);
	}

	public int getCoordY() {
		return centroCirculo.getNum2();
	}

	public void setCoordY(int coordY) {
		centroCirculo.setNum2(coordY);
	}

	public double getRadio() {
		return radio;
	}

	public void setRadio(double radio) {
		this.radio = radio;
	}

	public double devuelveArea(){
		double area;
		area=Math.PI*Math.pow(radio, 2);
		return area;
		
	}

	public double devuelveLongitud() {
		double longitud;
		longitud=2*Math.PI*radio;
		return longitud;
	}
	
	
	
}
