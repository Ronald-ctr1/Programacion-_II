public class TestAlgeVec {
    
    public static void main(String[] args) {
        double[] a = {1, 2, 3};
        double[] b = {2, 4, 6};

        AlgebraVectorial av = new AlgebraVectorial(a, b);

        System.out.println("¿Perpendicular (a · b = 0)? " + av.esPerpendicular());
        System.out.println("¿Perpendicular (|a+b| == |a-b|)? " + av.esPerpendicularPorNormasSumaResta());
        System.out.println("¿Perpendicular (|a-b| == |b-a|)? " + av.esPerpendicularPorSimetria());
        System.out.println("¿Perpendicular (|a+b|^2 == |a|^2 + |b|^2)? " + av.esPerpendicularPorTeoremaPitagoras());

        System.out.println("¿Paralelo (a × b = 0)? " + av.esParaleloPorCruzado());
        System.out.println("¿Paralelo (a = r * b)? " + av.esParaleloPorProporcion());

        System.out.println("Proyección de a sobre b: " + AlgebraVectorial.mostrarVector(av.proyeccion()));
        System.out.println("Componente de a en dirección de b: " + av.componente());
    }
}
