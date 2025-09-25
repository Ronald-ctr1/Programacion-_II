package Ejercicio2;
public class Aplicacion {
    public static void main(String[] args) {
        JuegoAdivinaNumero juegoNormal = new JuegoAdivinaNumero(3);
        JuegoAdivinaPar juegoPar = new JuegoAdivinaPar(3);
        JuegoAdivinaImpar juegoImpar = new JuegoAdivinaImpar(3);

        System.out.println("\n--- Juego Normal ---");
        juegoNormal.juega();

        System.out.println("\n--- Juego Par ---");
        juegoPar.juega();

        System.out.println("\n--- Juego Impar ---");
        juegoImpar.juega();
    }
}