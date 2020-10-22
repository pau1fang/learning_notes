#include<iostream>
#include<string>

void show_list(){}

template<typename T>
void show_list(const T &value)
{
    std::cout << value << '\n';
}
template<typename T, typename... Args>
void show_list(const T& value, const Args&... args)
{
    std::cout << value << ", ";
    show_list(args...);
}

int main()
{
    int n = 14;
    double x = 2.453553;
    std::string mr = "hello, world!";
    show_list(n,x);
    show_list(x*x,'!',3,mr);
    return 0;
}