#include <iostream>

int main()
{
    int n1, n2, n3;
    std::cout << "Enter 3 numbers:" << std::endl;
    std::cin >> n1 >> n2 >> n3;
    if (n1 > n2 && n1 > n3) {
        std::cout << "First Number is the max";
    } else if (n2 > n1 && n2 > n3) {
        std::cout << "Second Number is the max";
    } else if (n3 > n1 && n3 > n2) {
        std::cout << "Third Number is the max";
    } else {
        std::cout << "All numbers are equal";
    }
    return 0;
}