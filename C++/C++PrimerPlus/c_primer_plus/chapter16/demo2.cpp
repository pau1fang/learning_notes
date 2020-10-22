#include<iostream>
#include<vector>
int main()
{
    using std::cout;
    using std::endl;
    using std::vector;
    const int NUM = 5;
    vector<int> ratings(NUM);
    cout << ratings.capacity() << endl;
    cout << ratings.size() << endl;
    for (int i=0;i<NUM;i++)
        cout << ratings[i] << endl;
    for (int i=0;i<NUM;i++)
    {
        ratings[i] = i;
    }
    cout << ratings.capacity() << endl;
    cout << ratings.size() << endl;
    for (int i=0;i<NUM;i++)
        cout << ratings[i] << endl;
    return 0;
}