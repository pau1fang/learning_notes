#include<iostream>
#include<vector>
int main()
{
    using std::cout;
    using std::endl;
    using std::vector;
    const int NUM = 5;
    vector<int> ratings;
    for (int i=0;i<NUM;i++)
        ratings.push_back(i);
    cout << ratings.size() << endl;
    cout << ratings.capacity() << endl;
    auto pd = ratings.begin();
    cout << *pd << endl;
    for (auto pp = ratings.begin(); pp!=ratings.end(); pp++)
        cout << *pp << endl;
    
    return 0;
}