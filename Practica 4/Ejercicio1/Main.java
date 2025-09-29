import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Empleado[] empleados = new Empleado[5];

        System.out.println("Ingrese datos de 3 empleados a tiempo completo:");
        for (int i = 0; i < 3; i++) {
            System.out.print("Nombre del empleado " + (i + 1) + ": ");
            String nombre = scanner.nextLine();
            System.out.print("Salario anual: ");
            double salarioAnual = Double.parseDouble(scanner.nextLine());

            empleados[i] = new EmpleadoTiempoCompleto(nombre, salarioAnual);
        }

        System.out.println("\nIngrese datos de 2 empleados por hora:");
        for (int i = 3; i < 5; i++) {
            System.out.print("Nombre del empleado " + (i + 1) + ": ");
            String nombre = scanner.nextLine();
            System.out.print("Horas trabajadas: ");
            double horas = Double.parseDouble(scanner.nextLine());
            System.out.print("Tarifa por hora: ");
            double tarifa = Double.parseDouble(scanner.nextLine());

            empleados[i] = new EmpleadoTiempoHorario(nombre, horas, tarifa);
        }

        System.out.println("\nInformación de los empleados:");
        for (Empleado emp : empleados) {
            System.out.println(emp.toString() + " | Salario Mensual: " + emp.calcularSalarioMensual());
        }

        scanner.close();
    }
}
