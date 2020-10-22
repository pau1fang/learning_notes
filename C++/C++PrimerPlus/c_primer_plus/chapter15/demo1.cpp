#include<iostream>

int main()
{
    try
    {
        throw (5.0);
    }

    // std::cout << " hi " << std::endl;

    catch(const double a)
    {
        std::cout << a << std::endl;
    }
    
}