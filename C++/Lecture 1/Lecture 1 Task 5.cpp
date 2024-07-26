#include <iomanip>
#include <iostream>

int main()
{
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    for (int i = 1; i <= 12; i++) {
        std::cout << n << " x " << std::setw(2) << i << " = " << i * n << std::endl;
    }
    return 0;
}