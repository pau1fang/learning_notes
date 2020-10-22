#include<iostream>
#include<sstream>
#include<string>

int main()
{
    using namespace std;
    ostringstream outstr;
    string hdisk;
    getline(cin, hdisk);
    int cap;
    cin >> cap;
    outstr << "The hard disk " << hdisk << " has a capacity of "
            << cap << " gigabytes.\n";
    string result = outstr.str();
    cout << result;
    return 0;
}