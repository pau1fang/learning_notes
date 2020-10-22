#include <iostream>

class Demo
{
private:
    int x;
    int y;
public:
    Demo(int a, int b) {x = a;y=b;}
    void show() const { std::cout << x << ", " << y << std::endl;}
    friend std::ostream & operator<<(std::ostream & os, const Demo & d);
};

int main()
{
    Demo demo1(1,2);
    demo1.show();
    std::cout << demo1 << std::endl;
}

std::ostream & operator<<(std::ostream & os, const Demo & d)
{
    os << d.x << ", " << d.y;
    return os;
}