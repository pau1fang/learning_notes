#include<iostream>
#include<typeinfo>

int main()
{
    using namespace std;
    int a = 100;
    long b = 50;
    int res;
    res = a / b;
    cout << res << endl;
    cout << typeid(res).name() << endl;
}