/* https://www.jitbit.com/screensharing/#9026157028323334145
Realizza la classe Stella, composta da oggetti 
della classe Pentagono e oggetti della classe Triangolo. 
Le classi Pentagono e Triangolo sono entrambe figlie 
della classe Poligono, che possiede la funzione virtuale 
perimetro. La classe Triangolo possiede due costruttori, 
il primo ha un solo parametro ed è utilizzato per costruire 
triangoli equilateri, il secondo ha due parametri 
(base e lato obliquo) ed è utilizzato per costruire 
triangoli isosceli. 
Mostra un utilizzo dell'oggetto "stella" nel main.
- - - - - - - - - - - - - - - - - - - - - - - - - - 
ATTRIBUZIONE DEI PUNTEGGI

1. class Poligono = 20 pt
2. class Pentagono = 15 pt
3. class Triangolo = 30 pt
4. class Stella = 25 pt
5. leggibilità del codice = 10 pt
- - - - - - - - - - - - - - - - - - - - - - - - - - 
*/


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