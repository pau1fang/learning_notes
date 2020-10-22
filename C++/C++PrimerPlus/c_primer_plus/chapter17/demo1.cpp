#include<iostream>

int main()
{
    using std::cout;
    using std::endl;
    long val = 560031841;
    cout.write((char *) &val, sizeof (long));
    cout << endl;
    double num = 321.123456789;
    cout << num << endl;
    return 0;
}