#include <iostream>

using namespace std;

int main() {
    int x, y;
    cin >> x;
    cin >> y;
    int somma = x + y;
    cout << somma << "\n";
    if (somma > 10) {
        cout << "Maggiore\n";
    } else {
        cout << "Minore\n";
    }
    return 0;
}
