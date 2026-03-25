#include <stdio.h>

int main() {
    int x, y;
    printf("Inserire valori:\nx = ");
    scanf("%d", &x);
    printf("y = ");
    scanf("%d", &y);
    int somma = x + y;
    printf("La somma è %d\n", somma);
    if (somma > 10){
        printf("Maggiore\n");
    } else {
        printf("Minore\n");
    }
    return 0;
}