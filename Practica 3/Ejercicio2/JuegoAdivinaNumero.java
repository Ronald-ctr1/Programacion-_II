package Ejercicio2;
import java.util.Scanner;

class JuegoAdivinaNumero {
    public int vidas;
    public int numeroSecreto;
    public Scanner sc;

    public JuegoAdivinaNumero(int vidas) {
        this.vidas = vidas;
        this.sc = new Scanner(System.in);
        this.numeroSecreto = (int)(Math.random() * 11);
    }

    public boolean validaNumero(int num) {
        return num >= 0 && num <= 10;
    }

    public void juega() {
        System.out.println("Juego de adivinar número entre 0 y 10. Tienes " + vidas + " vidas.");
        while (vidas > 0) {
            System.out.print("Introduce un número: ");
            int intento = sc.nextInt();

            if (!validaNumero(intento)) {
                System.out.println("Número inválido. Debe estar entre 0 y 10.");
                continue;
            }

            if (intento == numeroSecreto) {
                System.out.println("¡Correcto! Has adivinado el número.");
                return;
            } else {
                vidas--;
                System.out.println("Incorrecto. Te quedan " + vidas + " vidas.");
            }
        }
        System.out.println("Has perdido. El número era: " + numeroSecreto);
    }
}