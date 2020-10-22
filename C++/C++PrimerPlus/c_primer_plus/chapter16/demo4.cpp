#include<iostream>
#include<algorithm>

int main()
{
    using std::cout;
    using std::endl;
    using std::sort;
    double ar[5] = {2,1,7,4,3};
    for (double i:ar)
        cout << i << endl;
    sort(ar, ar+5);
    for (double i: ar)
        cout << i << endl;
    return 0;
}