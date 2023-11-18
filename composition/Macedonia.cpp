/*
Realizza la classe Macedonia, composta da oggetti della classe Mela e della classe Pesca. 
Le classi Mela e Pesca sono entrambe figlie della classe Frutto, che possiede la funzione 
virtuale volume. Il metodo volume ha come parametro il peso del frutto. 
Entrambe le classi implementano un costruttore che ha come parametro il peso specifico del 
frutto, presente solo se questo è diverso dal valore di default. 
Per semplicità possiamo considerare il peso specifico di default della mela pari a 300kg/dm3 
e della pesca pari a 350 kg/dm3.

La classe Pesca possiede un secondo costruttore che ha un secondo parametro (per facilità 
può essere di tipo intero) utilizzato per specificare la varietà dell’oggetto pesca (es. 
gialla, bianca, saturnina, ecc.). 

Mostra un utilizzo dell'oggetto "macedonia" nel main, in particolare fornisci un metodo alla 
classe Macedonia per conoscere quanto volume occupa l'oggetto creato.

PS: il volume è dato dal rapporto tra il peso e il peso specifico.

- - - - - - - - - - - - - - - - - - - - - - - - - - 

ATTRIBUZIONE DEI PUNTEGGI

1. class Frutto = 20 pt
2. class Mela = 20 pt
3. class Pesca = 25 pt
4. class Macedonia = 25 pt
5. documentazione/leggibilità codice = 10 pt

- - - - - - - - - - - - - - - - - - - - - - - - - - 
*/

#include <iostream>

using namespace std;

class Frutto
{
protected:
    int pesoSpecifico;
    float peso;
    virtual float volume(float pPeso) = 0;
public:
    float getPeso()
    {
        return peso;
    }
// - - - - FACOLTATIVO - - - - 
    int getPesoSpecifico()
    {
        return pesoSpecifico;
    }
// - - - - - - - - - - - - - -
};

class Mela : public Frutto
{
public:
    Mela(int pPesoSpecifico = 300)
    {
        pesoSpecifico = pPesoSpecifico;
    }
    float volume(float pPeso)
    {
        peso = 1.0 * pPeso;
        return peso/pesoSpecifico;
    }
};

class Pesca : public Frutto
{
    int varieta;
public:
    Pesca(int pPesoSpecifico = 350) 
    {
        pesoSpecifico = pPesoSpecifico;
    }
    Pesca(int pVarieta, int pPesoSpecifico = 350) 
    {
        pesoSpecifico = pPesoSpecifico;
        varieta = pVarieta;
    }
    float volume(float pPeso)
    {
        peso = 1.0 * pPeso;
        return peso/pesoSpecifico;
    }
};

class Macedonia
{
private:
    Mela mela;
    Pesca pesca;
    float volumeMela, volumePesca;
public:
    Macedonia(Mela pMela, float pPesoMela, Pesca pPesca, float pPesoPesca)
    {
        mela = pMela;
        pesca = pPesca;
        volumeMela = mela.volume(pPesoMela);
        volumePesca = pesca.volume(pPesoPesca);
    }
    float volumeMacedonia()
    {
        return volumeMela + volumePesca;
    }
};


int main()
{
    Mela m;
    Mela n = Mela(400);
    Pesca p = Pesca(2, 250);
    Pesca q;
    
    Macedonia a = Macedonia(m, 0.4, p, 0.2);
    Macedonia b = Macedonia(n, 0.3, q, 0.25);
    cout << "\n* VOLUME MACEDONIA *\n";
    cout << "- A\t" << a.volumeMacedonia() << endl;
    cout << "- B\t" << b.volumeMacedonia() << endl;
    cout << endl;
    return 0;
}
