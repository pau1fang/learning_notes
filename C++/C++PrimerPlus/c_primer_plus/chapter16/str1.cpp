#include<iostream>
#include<string>

int main()
{
    using namespace std;
    string one("Lottery Winner!");
    cout << one << endl;
    string two(20, '$');
    cout << two << endl;
    string three(one);
    cout << three << endl;
    one += " Oops!";
    cout << one << endl;
    two = "Sorry! That was ";
    three[0] = 'P';
    string four;
    four = two + three;
    cout << four << endl;
    char alls[] = "All's well that ends well";
    string five(alls, 20);
    cout << five << endl;
    string five1(alls, 40);
    cout << five1 << endl;
    return 0;
}