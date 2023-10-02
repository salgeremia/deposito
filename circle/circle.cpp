#include <iostream>

using namespace std;

class Circle
{
private:
    int x, y, radius;
public:
    Circle(int pX, int pY, int pRadius)
    {
        x = pX;
        y = pY;
        radius = pRadius;
        cout << "Object created." << endl;
    }
    ~Circle()
    {
        cout << "Object destroyed." << endl;
    }
    void info()
    {
        cout << "*** INFO ***\n";
        cout << "- centre:\nX = " << x << "\nY = " << y << endl;
        cout << "- radius: " << radius << endl;
    }
};


int main()
{
    Circle c = Circle(3, 5, 2);
    c.info();
    c.~Circle();
    return 0;
}
