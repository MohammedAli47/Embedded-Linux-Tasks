#include <iostream>

int main()
{
    int sum = 0;
    std::string num;
    std::cout << "Enter a number: ";
    std::cin >> num;
    for (char c : num) {
        sum += (c - '0');
    }
    std::cout << "Sum of digits = " << sum;
    return 0;
}