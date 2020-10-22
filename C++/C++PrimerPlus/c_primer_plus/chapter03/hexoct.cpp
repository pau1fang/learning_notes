#include<iostream>
int main()
{
	using namespace std;
	int chest = 42;
	int waist{0x42};
	int inseam = {042};

	cout << "Monsieur cuts a striking figure!\n";
	cout << "chest = " << chest << endl;
	cout << "waist = " << waist << endl;
	cout << "inseam = " << inseam << endl;
	return 0;
}
