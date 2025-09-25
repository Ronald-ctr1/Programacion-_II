package Ejercicio1;
public class Juego {
    public int numeroDeVida;
    public int record;

    public Juego(int numeroDeVida) {
        this.numeroDeVida = numeroDeVida;
        this.record = 0;
    }

    public void reiniciaPartida() {
        System.out.println("Partida reiniciada.");
    }

    public void actualizaRecord() {
        record++;
        System.out.println("¡Nuevo récord! Puntos: " + record);
    }

    public boolean quitaVida() {
        numeroDeVida--;
        if (numeroDeVida > 0) {
            System.out.println("Te quedan " + numeroDeVida + " vidas.");
            return true;
        } else {
            System.out.println("¡No te quedan vidas!");
            return false;
        }
    }
}
