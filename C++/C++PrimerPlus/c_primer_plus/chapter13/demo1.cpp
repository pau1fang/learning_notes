#include<iostream>
using std::cout;
using std::endl;

class Employee
{
private:
    int num;
public:
    Employee(int n=0) { num = n; }
    void show_num() {cout << num << endl;}
};

class Singer : public Employee
{
public:
    Singer(int n = 0) : Employee(n) {}
    void range() { cout << "hello"<< endl;}
};

int main()
{
    Employee e1(1);
    Singer s1(2);
    e1.show_num();
    s1.show_num();
    s1.range();
    Employee * e2 = &s1;
    e2->show_num();
    Singer *s2;
    s2 = (Singer *) &e1;
    s2->range();
    cout << sizeof *s2 << endl;
    cout << sizeof *e2 << endl;
}