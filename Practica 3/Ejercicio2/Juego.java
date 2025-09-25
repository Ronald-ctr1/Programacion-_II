package Ejercicio2;
public class Juego {
    public int numeroDeVidas;
    public int record;

    public void reiniciaPartida() {
        System.out.println("Reiniciando partida...");
        numeroDeVidas = 3;
    }

    public void actualizaRecord() {
        System.out.println("¡Nuevo récord!");
        record++;
    }

    public boolean quitaVida() {
        numeroDeVidas--;
        if (numeroDeVidas > 0) {
            System.out.println("Te quedan " + numeroDeVidas + " vidas.");
            return true;
        } else {
            System.out.println("¡Has perdido todas tus vidas!");
            return false;
        }
    }
}
