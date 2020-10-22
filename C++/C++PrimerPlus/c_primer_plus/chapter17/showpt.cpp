#include<iostream>

int main()
{
    using std::cout;
    using std::ios_base;

    float price1 = 20.40;
    float price2 = 1.9+8.0/9.0;

    cout.setf(ios_base::showpoint);
    cout << price1 << "\n" << price2 << "\n";
    cout.precision(2);
    cout << price1 << "\n" << price2 <<"\n";
    return 0;
}