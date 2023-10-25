#include <iostream>

using namespace std;

class Poligono
{
protected:
    Poligono()
    {
        cout << "Creazione poligono: ";
    }
    virtual int perimetro() = 0;
};

class Pentagono : Poligono
{
    int lato;
public:
    Pentagono() : Poligono()
    {
        cout << "PENTAGONO VUOTO" << endl;
    }
    Pentagono(int pLato) : Poligono()
    {
        lato = pLato;
        cout << "PENTAGONO" << endl;
    }
    int perimetro()
    {
        return lato*5;
    }
};

class Triangolo : Poligono
{
    int base, latoObliquo;
public:
    Triangolo() : Poligono()
    {
        cout << "TRIANGOLO VUOTO" << endl;
    }
    Triangolo(int pBase) : Poligono()
    {
        base = pBase;
        latoObliquo = pBase;
        cout << "TRIANGOLO EQUILATERO" << endl;
    }
    Triangolo(int pBase, int pLatoObliquo) : Poligono()
    {
        base = pBase;
        latoObliquo = pLatoObliquo;
        cout << "TRIANGOLO ISOSCELE" << endl;
    }
    int perimetro()
    {
        return base + latoObliquo*2;
    }
};

class Stella
{
    Pentagono pentagono;
    Triangolo triangolo;
public:
    Stella(Pentagono pPentagono, Triangolo pTriangolo)
    {
        pentagono = pPentagono;
        triangolo = pTriangolo;
    }
    int perimetro()
    {
        return triangolo.perimetro()*5 - pentagono.perimetro();
    }
};


int main()
{
    Pentagono p = Pentagono(3);
    Triangolo t = Triangolo(3, 4);
    Stella stella = Stella(p, t);
    cout << "Il perimetro della STELLA è " << stella.perimetro() << endl;
}

