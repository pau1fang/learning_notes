#include <iostream>
#include "tabtenn1.h"

void Show(const TableTennisPlayer &);
int main()
{
    using std::cout;
    using std::endl;
    TableTennisPlayer player1("Tara", "Boomdea", false);
    RatedPlayer rplayer1(1140, "Mallory", "Duck", true);
    Show(player1);
    Show(rplayer1);

    RatedPlayer p1(1840, "p1", "p1", true);
    TableTennisPlayer p2(p1);
    p2.Name();
    cout << p2.HasTable() << endl;
}

void Show(const TableTennisPlayer & rt)
{
    using std::cout;
    cout << "Name: ";
    rt.Name();
    cout << "\nTable: ";
    if (rt.HasTable())
        cout << "yes\n";
    else
        cout << "no\n";
}