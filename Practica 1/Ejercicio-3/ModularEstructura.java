import java.util.Scanner;

public class ModularEstructura {

    public static double promedio(double[] numeros) {
        double suma = 0;
        for (double num : numeros) {
            suma += num;
        }
        return suma / numeros.length;
    }

    public static double desviacion(double[] numeros) {
        double prom = promedio(numeros);
        double suma = 0;
        for (double num : numeros) {
            suma += Math.pow(num - prom, 2);
        }
        return Math.sqrt(suma / (numeros.length - 1));
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double[] datos = new double[10];

        System.out.println("Ingrese 10 números:");
        for (int i = 0; i < 10; i++) {
            datos[i] = input.nextDouble();
        }

        double promedio = promedio(datos);
        double desviacion = desviacion(datos);

        System.out.printf("El promedio es: %.2f\n", promedio);
        System.out.printf("La desviación estándar es: %.5f\n", desviacion);

        input.close();
    }
}
