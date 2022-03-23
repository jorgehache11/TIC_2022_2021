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
	public String getMes(int modo) {
		String nombreMes="";
		if(modo==0) {
			if(this.mes==1) nombreMes="Enero";
			if(this.mes==2) nombreMes="Febrero";
			if(this.mes==3) nombreMes="Marzo";
			if(this.mes==4) nombreMes="Abril";
			if(this.mes==5) nombreMes="Mayo";
			if(this.mes==6) nombreMes="Junio";
			if(this.mes==7) nombreMes="Julio";
			if(this.mes==8) nombreMes="Agosto";
			if(this.mes==9) nombreMes="Septiembre";
			if(this.mes==10) nombreMes="Octubre";
			if(this.mes==11) nombreMes="Noviembre";
			if(this.mes==12) nombreMes="Diciembre";
		}
		if(modo==1) {
			if(this.mes==1) nombreMes="ENERO";
			if(this.mes==2) nombreMes="FEBRERO";
			if(this.mes==3) nombreMes="MARZO";
			if(this.mes==4) nombreMes="ABRIL";
			if(this.mes==5) nombreMes="MAYO";
			if(this.mes==6) nombreMes="JUNIO";
			if(this.mes==7) nombreMes="JULIO";
			if(this.mes==8) nombreMes="AGOSTO";
			if(this.mes==9) nombreMes="SEPTIEMBRE";
			if(this.mes==10) nombreMes="OCTUBRE";
			if(this.mes==11) nombreMes="NOVIEMBRE";
			if(this.mes==12) nombreMes="DICIEMBRE";
		}
		return nombreMes;
	}
	public void setMes(int mes) {
		this.mes = mes;
	}
	
	public void setMes(String nombreMes) {
		if(nombreMes=="Enero") this.mes=1;
		if(nombreMes=="Febrero") this.mes=2;
		if(nombreMes=="Marzo") this.mes=3;
		if(nombreMes=="Abril") this.mes=4;
		if(nombreMes=="Mayo") this.mes=5;
		if(nombreMes=="Junio") this.mes=6;
		if(nombreMes=="Julio") this.mes=7;
		if(nombreMes=="Agosto") this.mes=8;
		if(nombreMes=="Septiembre") this.mes=9;
		if(nombreMes=="Octubre") this.mes=10;
		if(nombreMes=="Noviembre") this.mes=11;
		if(nombreMes=="Diciembre") this.mes=12;			
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
