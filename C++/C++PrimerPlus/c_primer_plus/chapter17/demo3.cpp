#include<iostream>

int main()
{
    using namespace std;
    char line[50];
    cin.get(line, 50);
    char ch;
    cin.get(ch);
    cout << line << endl;
    cout << ch << endl;

    char line2[50];
    char ch2;
    cin.getline(line2, 50);
    cin.get(ch2);
    return 0;
}