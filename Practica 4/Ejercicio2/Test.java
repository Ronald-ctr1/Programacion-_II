import java.util.Random;

public class Test {
    public static void main(String[] args) {
        Figura[] figuras = new Figura[5];
        Random rand = new Random();

        for (int i = 0; i < figuras.length; i++) {
            int tipo = rand.nextInt(2) + 1; 
            String color = (rand.nextBoolean()) ? "Rojo" : "Azul";

            if (tipo == 1) {
                double lado = rand.nextDouble() * 10 + 1;
                figuras[i] = new Cuadrado(lado, color);
            } else {
                double radio = rand.nextDouble() * 10 + 1;
                figuras[i] = new Circulo(radio, color);
            }
        }

        for (Figura f : figuras) {
            System.out.println(f.toString());
            System.out.printf("Área: %.2f\n", f.area());
            System.out.printf("Perímetro: %.2f\n", f.perimetro());

            if (f instanceof Coloreado) {
                Coloreado c = (Coloreado) f;
                System.out.println("Cómo colorear: " + c.comoColorear());
            }

            System.out.println("---------------------------");
        }
    }
}
