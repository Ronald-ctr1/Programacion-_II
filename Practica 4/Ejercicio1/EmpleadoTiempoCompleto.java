public class EmpleadoTiempoCompleto extends Empleado {
    private double salarioAnual;

    public EmpleadoTiempoCompleto(String nombre, double salarioAnual) {
        super(nombre);
        this.salarioAnual = salarioAnual;
    }

    @Override
    public double calcularSalarioMensual() {
        return salarioAnual / 12;
    }

    @Override
    public String toString() {
        return super.toString() + " -Tipo: Tiempo Completo - Salario Anual: " + salarioAnual;
    }
}
