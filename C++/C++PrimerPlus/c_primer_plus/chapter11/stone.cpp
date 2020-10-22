#include <iostream>
using std::cout;
#include "stonewt.h"
void display(const Stonewt & st, int n);
int main()
{
    Stonewt incognito = 275;
    Stonewt wolfe(285.7);
    Stonewt taft(21, 8);

    incognito.show_stn();
    wolfe.show_stn();
    taft.show_lbs();
    incognito = 276.8;
    taft = 325;
    incognito.show_stn();
    taft.show_lbs();
    display(taft, 2);
    display(422, 2);
    return 0;
}

void display(const Stonewt & st, int n)
{
    for (int i = 0; i< n;i++)
    {
        cout << "Wow! ";
        st.show_stn();
    }
}