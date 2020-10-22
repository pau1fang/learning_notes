#include<iostream>
#include<utility>

// int func_add(int &);
int func_add(int &&);

int main()
{
    int a = 10;
    func_add(std::move(a));
    func_add(5);
    return 0;
}

int func_add(int & a)
{
    a += 10;
    std::cout << a << std::endl;
    return 0;
}

int func_add(int && a)
{
    a += 10;
    std::cout << a << std::endl;
    return 0;
}