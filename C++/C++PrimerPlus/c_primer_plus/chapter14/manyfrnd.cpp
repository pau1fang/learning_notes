#include<iostream>
using std::cout;
using std::endl;

template<typename T>
class ManyFriend
{
private:
    T item;
public:
    ManyFriend(const T & i) : item(i) {}
    template<typename C, typename D> friend void show(C &, D &);
};

template<typename C, typename D>
void show(C & c, D & d)
{
    cout << c.item << ", " << d.item << endl;
}

int main()
{
    ManyFriend<int> hfi1(10);
    ManyFriend<int> hfi2(20);
    ManyFriend<double> hfdb(10.5);
    show(hfi1, hfi2);
    show(hfdb, hfi1);
}