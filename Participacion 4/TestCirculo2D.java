public class TestCirculo2D {
    public static void main(String[] args){
        Circulo2D c1 = new Circulo2D(2,0,1);

        System.out.println("Area: "+ c1.getArea());
        System.out.println("Perimetro: "+c1.getPerimetro());

        System.out.println("Contiene el punto (2.5, 0) ?"+ c1.contiene(2.5,0));
        System.out.println("Contiene el circulo (2,0,0.5)?"+ c1.contiene(new Circulo2D(2,0,0.5)));
        System.out.println("Se sobrepone con el ciculo (0,0,2)?" + c1.sobrepone(new Circulo2D(0,0,2)));
    }
}
