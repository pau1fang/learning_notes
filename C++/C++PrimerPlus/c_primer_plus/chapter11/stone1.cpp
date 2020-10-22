#include <iostream>
#include "stonewt1.h"

int main()
{
    using std::cout;
    Stonewt poppins(9,2.8);
    double p_wt = poppins;
    cout << p_wt << std::endl;
    cout << int (poppins) << std::endl;
    return 0;
}