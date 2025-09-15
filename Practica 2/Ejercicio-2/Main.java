public class Main {
    public static void main(String[] args) {
        Vector3D a = new Vector3D(1, 2, 3);
        Vector3D b = new Vector3D(4, -5, 6);

        System.out.println("Vector a: " + a);
        System.out.println("Vector b: " + b);

        System.out.println("a + b = " + a.add(b));
        System.out.println("2 * a = " + a.multiply(2));
        System.out.printf("|a| = %.3f%n", a.magnitude());
        System.out.println("Normalizado a = " + a.normalize());
        System.out.printf("a · b = %.3f%n", a.dot(b));
        System.out.println("a × b = " + a.cross(b));
        System.out.println("¿a ortogonal a b? " + (a.isOrthogonalTo(b) ? "Sí" : "No"));
        System.out.println("¿El paralelogramo formado por a y b es rectángulo? " + (a.formsRectangleWith(b) ? "Sí" : "No"));
        System.out.println("Proyección de a sobre b: " + a.projectionOn(b));
        System.out.println("Componente ortogonal de a respecto a b: " + a.orthogonalComponent(b));
    }
}
