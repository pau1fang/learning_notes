#include<iostream>
const int Limit = 255;
int main()
{
    using namespace std;
    char input[Limit];
    cin.getline(input, Limit, '#');
    cout << input << "\n";
    char ch;
    cin.get(ch);
    cout << ch << endl;
    if (ch != '\n')
    {
        cin.ignore(Limit, '\n');
    }
    cin.get(input, Limit, '#');
    cout << input << "\n";
    cin.get(ch);
    cout << ch << endl;
    return 0;
}