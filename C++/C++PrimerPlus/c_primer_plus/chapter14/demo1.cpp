#include<iostream>
#include "arraytp.h"

int main()
{
    using std::cout;
    using std::endl;
    ArrayTP<int, 100> sums;
    cout << sizeof sums << endl;
    sums.Size();
}