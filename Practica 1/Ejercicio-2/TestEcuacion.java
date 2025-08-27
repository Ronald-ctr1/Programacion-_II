import java.util.Scanner;
public class TestEcuacion {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Ingrese a, b, c: ");
        double a = input.nextDouble();
        double b = input.nextDouble();
        double c = input.nextDouble();

        Ecuacion eq = new Ecuacion(a, b, c);
        double discriminante = eq.getDiscriminante();

        if (discriminante > 0) {
            System.out.printf("La ecuación tiene dos raíces %.6f y %.6f \n", eq.getRaiz1(), eq.getRaiz2());
        } else if (discriminante == 0) {
            System.out.printf("La ecuación tiene una raíz %.6f \n", eq.getRaiz1());
        } else {
            System.out.println("La ecuación no tiene raíces reales");
        }

        input.close();
    }
}
