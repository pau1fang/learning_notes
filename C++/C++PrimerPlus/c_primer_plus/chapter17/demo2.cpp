#include<iostream>
int main()
{
    using std::cout;
    using std::endl;
    using std::cin;
    int ct = 0;
    char ch;
    cin.get(ch);
    while (ch != '\n')
    {
        cout << ch;
        ct++;
        cin.get(ch);
    }
    cout << "\n";
    cout << ct << endl;
    return 0;
}