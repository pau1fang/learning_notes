#include<iostream>
class bad_hmean
{
private:
    double x;
    double y;
public:
    bad_hmean(double a = 0, double b = 0):x(a), y(b) {}
    void mesg();
};

inline void bad_hmean::mesg()
{
    std::cout << "hmean(" << x << ", " << y << "): " << "invalid arguments: a=-b\n";
}

class bad_gmean
{
public:
    double x;
    double y;
    bad_gmean(double a = 0, double b = 0):x(a), y(b) {}
    const char * mesg();
};

inline const char * bad_gmean::mesg()
{
    return "gmean() arguments should be>=0\n";
}