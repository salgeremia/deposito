#include <iostream>
using namespace std;

class Cerchio 
{
    double x, y;
    public:
    void centro(){
        cout << "Le coordinate del centro sono:\n";
        cout << "X: " << x << endl << "Y: " << y << endl;
    }
    Cerchio(double pX, double pY){
        x = pX;
        y = pY;
        cout << "Nuovo CERCHIO costruito.\n";
    }
    ~Cerchio(){
        cout << "L'oggetto è stato distrutto.\n";
    }
};

int main()
{
    Cerchio c = Cerchio(0, 0);
    // c.centro();
    delete c;
    cout << "..." << endl;
    c.centro();
    return 0;
}
