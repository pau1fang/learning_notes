#include<iostream>
#include<memory>
#include<string>

int main()
{
    using namespace std;
    unique_ptr<string> p1(new string("auto"));
    unique_ptr<string> p2;
    cout << *p1 << endl;
    cout << *p2 << endl;
    return 0;
}