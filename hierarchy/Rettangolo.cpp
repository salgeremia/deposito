#include <iostream>

using namespace std;

class Rettangolo
{
private:
    int base, altezza;
public:
    int area()
    {
        return base*altezza;
    }
    int perimetro()
    {
        return (base+altezza)*2;
    }
    Rettangolo(int pBase, int pAltezza)
    {
        base = pBase;
        altezza = pAltezza;
    }
};

class Quadrato : public Rettangolo
{
private:
    int lato;
public:
    Quadrato(int pLato) : Rettangolo(pLato, pLato)
    {
        lato = pLato;
    }

};

int main()
{
    Rettangolo r = Rettangolo(4,5);
    Quadrato q = Quadrato(6);
    cout << r.area() << " - " << r.perimetro() << endl;
    cout << q.area() << " - " << q.perimetro();
    return 0;
}


