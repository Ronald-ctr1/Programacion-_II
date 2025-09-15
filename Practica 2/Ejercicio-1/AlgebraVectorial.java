import java.util.Arrays;

public class AlgebraVectorial {
    private double[] a;
    private double[] b;

    public AlgebraVectorial() {
        this.a = new double[]{0, 0, 0};
        this.b = new double[]{0, 0, 0};
    }

    public AlgebraVectorial(double[] a, double[] b) {
        this.a = a;
        this.b = b;
    }

    private double[] suma(double[] u, double[] v) {
        return new double[]{
            u[0] + v[0],
            u[1] + v[1],
            u[2] + v[2]
        };
    }

    private double[] resta(double[] u, double[] v) {
        return new double[]{
            u[0] - v[0],
            u[1] - v[1],
            u[2] - v[2]
        };
    }

    private double productoPunto(double[] u, double[] v) {
        return u[0]*v[0] + u[1]*v[1] + u[2]*v[2];
    }

    private double norma(double[] v) {
        return Math.sqrt(productoPunto(v, v));
    }

    private double[] productoCruzado(double[] u, double[] v) {
        return new double[]{
            u[1]*v[2] - u[2]*v[1],
            u[2]*v[0] - u[0]*v[2],
            u[0]*v[1] - u[1]*v[0]
        };
    }

    private boolean esVectorCero(double[] v) {
        return v[0] == 0 && v[1] == 0 && v[2] == 0;
    }

    private boolean sonIguales(double x, double y) {
        return Math.abs(x - y) < 1e-6;
    }

    public boolean esPerpendicular() {
        return sonIguales(productoPunto(a, b), 0);
    }

    public boolean esPerpendicularPorNormasSumaResta() {
        return sonIguales(norma(suma(a, b)), norma(resta(a, b)));
    }

    public boolean esPerpendicularPorSimetria() {
        return sonIguales(norma(resta(a, b)), norma(resta(b, a)));
    }

    public boolean esPerpendicularPorTeoremaPitagoras() {
        double sumaNorma2 = Math.pow(norma(suma(a, b)), 2);
        double sumaIndiv = Math.pow(norma(a), 2) + Math.pow(norma(b), 2);
        return sonIguales(sumaNorma2, sumaIndiv);
    }

    public boolean esParaleloPorCruzado() {
        return esVectorCero(productoCruzado(a, b));
    }

    public boolean esParaleloPorProporcion() {
        Double razon = null;
        for (int i = 0; i < 3; i++) {
            if (b[i] != 0) {
                double r = a[i] / b[i];
                if (razon == null) {
                    razon = r;
                } else if (!sonIguales(razon, r)) {
                    return false;
                }
            } else if (a[i] != 0) {
                return false;
            }
        }
        return true;
    }

    public double[] proyeccion() {
        double dot = productoPunto(a, b);
        double normaB2 = Math.pow(norma(b), 2);
        double escalar = dot / normaB2;
        return new double[]{escalar * b[0], escalar * b[1], escalar * b[2]};
    }

    public double componente() {
        return productoPunto(a, b) / norma(b);
    }

    public static String mostrarVector(double[] v) {
        return Arrays.toString(v);
    }
}
