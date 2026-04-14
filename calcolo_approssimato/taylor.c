#include <stdio.h>

int main() {
    // base ^ esponente
    // ----------------
    //    esponente!
    int esponente = 3;
    int base = 4;
    

    for(int e = 0; e <= esponente; e++){
        int potenza = 1;
        int fattoriale = 1;

        // Calcolo la potenza
        for(int i = 0; i < e; i++){
            potenza *= base;
        }
        printf("POTENZA = %d\n", potenza);

        // Calcolo il fattoriale
        for(int i = e; i > 0; i--){
            fattoriale *= i;
        }
        printf("FATTORIALE = %d\n", fattoriale);

        // Calcolo l'approssimazione
        printf("%d. APPROSSIMAZIONE = %f\n", e+1, (float)potenza/fattoriale);
    }

    return 0;
}