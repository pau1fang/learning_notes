#include<iostream>
#include "somedefs.h"
#include<functional>

double dub(double x) { return 2.0*x; }
double square(double x) { return x*x; }

int main()
{
    using std::cout;
    using std::endl;
    using std::function;

    double y = 1.21;
    typedef function<double(double)> fdd;
    cout << " " << use_f(y, fdd(dub)) << endl;
    cout << " " << use_f(y, fdd(square)) << endl;
    cout << " " << use_f(y, fdd(Fp(10.0))) << endl;
    cout << " " << use_f(y, fdd(Fq(10.0))) << endl;
    cout << " " << use_f(y, fdd([] (double u) {return u*u;})) << endl;
    cout << " " << use_f(y, fdd([] (double u) { return u+u/2.0; })) << endl;
    return 0;
}