public abstract class Empleado {
    protected String nombre;

    public Empleado(String nombre) {
        this.nombre = nombre;
    }

    public abstract double calcularSalarioMensual();

    public String toString() {
        return "Nombre: " + nombre;
    }
}
