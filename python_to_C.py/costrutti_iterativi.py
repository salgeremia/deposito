# COSTRUTTO ITERATIVO DEFINITO: for
a = int(input('Inserire primo valore: ')) 
b = int(input('Inserire secondo valore: '))
somma_dispari = 0
for i in range(a, b+1):
    if i%2 == 1:
        somma_dispari += i
print('La somma dei valori dispari contenuti nell\'intervallo [a, b] =', somma_dispari)
'''
int a, b, somma_dispari = 0;
printf("Inserire primo valore: ");          |   cout << "Inserire primo valore: ";
scanf("%d", &a);                            |   cin >> a;
printf("Inserire secondo valore: ");        |   cout << "Inserire secondo valore: ";
scanf("%d", &b);                            |   cin >> b;
for(int i=a; i<=b; i++){
    if(i%2 == 1){
        somma_dispari += i;
    }
}
printf("La somma...%d\n", somma_dispari);   |   cout << "La somma..." << somma_dispari << endl;   
'''

# COSTRUTTO ITERATIVO INDEFINITO: while
n = int(input('Inserisci un valore intero.\nn = '))
while n!=1:
    print(n, '->', end=' ')
    n //= 2
print(1)
'''
int n;
printf("Inserisci un valore intero.\nn = ");    |   cout << "Inserisci un valore intero.\nn = ";
scanf("%d", &n);                                |   cin >> n;
while(n!=1){
    printf("%d -> ", n);                        |   cout << n << " -> ";
    n /= 2;
}
print("1\n");                                   |   cout << 1 << endl;
'''

# COSTRUTTO ITERATIVO INDEFINITO: do-while
print('Inserisci una sequenza di numeri interi.\nPer terminare inserisci lo 0.')
while True:
    n = int(input('n = '))
    if n == 0:
        break
    print('La metà di', n, 'è', n/2)
print('Sequenza terminata.')
'''
int n;
printf("Inserisci...\nPer terminare...\n");     |   cout << "Inserisci...\nPer terminare..." << endl;
do{
    printf("n = ");                             |   cout << "n = ";
    scanf("%d", &n);                            |   cin >> n;
    if(n == 0){
        break;
    }
    print("La metà di %d è %f")...              |   cout << "La metà di " << n << " è " << n/2.0 << endl;
} while(n != 0);
printf("Sequenza terminata.\n");                |   cout << "Sequenza terminata." << endl;
'''