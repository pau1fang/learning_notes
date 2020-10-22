#include<iostream>
#include "somedefs2.h"

double dub(double x) {return 2.0*x;}
double square(double x) { return x*x;}

int main()
{
    using std::cout;
    using std::endl;

    double y = 1.21;
    cout << "Function pointer dub:\n";
    cout << " " << use_f<double>(y, dub) << endl;
    cout << "Function pointer square:\n";
    cout << " " << use_f<double>(y, square) << endl;
    cout << "Funcion object Fp:\n";
    cout << " " << use_f<double>(y, Fp(5.0)) << endl;
    cout << "Function object Fq:\n";
    cout << " " << use_f<double>(y, Fq(5.0)) << endl;
    cout << "Lambda expression 1:\n";
    cout << " " << use_f<double>(y, [](double x){return x*x;}) << endl;
    cout << "Lambda expression 2:\n";
    cout << " " << use_f<double>(y,[](double x){ return x+x/2.0;}) << endl;
    return 0;
}