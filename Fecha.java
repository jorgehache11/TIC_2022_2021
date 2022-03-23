package MiCodigo;

public class Fecha {
	//ATRIBUTOS
	private int dia;
	private int mes;
	private int anio;


	//CONSTRUCTOR
	public Fecha(int dia, int mes, int anio) {
		super();
		this.dia = dia;
		this.mes = mes;
		this.anio = anio;
	}

	//METODOS
	public int getDia() {
		return dia;
	}
	public void setDia(int dia) {
		this.dia = dia;
	}
	public int getMes() {
		return mes;
	}
	public void setMes(int mes) {
		this.mes = mes;
	}
	public int getAnio() {
		return anio;
	}
	public void setAnio(int anio) {
		this.anio = anio;
	}

	boolean esPosterior(Fecha nuevaFecha){
	boolean loEs;//Ponemos esto para tener q evitar poner tantos else
	loEs=false;

	if(this.getAnio()>nuevaFecha.getAnio()) loEs=true;
	else 
		if(this.getAnio()==nuevaFecha.getAnio()) 
			if(this.getMes()>nuevaFecha.getMes()) 
				loEs=true;
			else 
				if(this.getMes()==nuevaFecha.getMes()) 
					if(this.getDia()>nuevaFecha.getDia()) 
						loEs=true;
	
	return loEs;
	}
}
