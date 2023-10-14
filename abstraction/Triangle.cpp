#include <iostream>

using namespace std;

class Triangolo
{
protected:
    int l1, l2, l3;
    virtual int perimetro() = 0;
};

class Equilatero : Triangolo
{
public:
    int perimetro()
    {
        return l1*3;
    }
    Equilatero(int pLato)
    {
        l1 = pLato;
    }
};

class Scaleno : Triangolo
{
private:
    /* data */
public:
    int perimetro()
    {
        return l1 + l2 + l3;
    }
    Scaleno(int pL1, int pL2, int pL3)
    {
        l1 = pL1;
        l2 = pL2;
        l3 = pL3;
    }
};


int main()
{
    Equilatero e = Equilatero(7);
    int p = e.perimetro();
    cout << "Perimetro = " << p << endl;

    Scaleno s = Scaleno(3, 4, 5);
    p = s.perimetro();
    cout << "Perimetro = " << p << endl;

    return 0;
}



