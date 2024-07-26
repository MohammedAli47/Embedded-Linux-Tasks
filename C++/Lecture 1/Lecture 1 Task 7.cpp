#include <bitset>
#include <iostream>

int main()
{
    int num;
    std::cout << "Enter a decimal number: ";
    std::cin >> num;
    std::bitset<8> s(num);
    std::cout << "Binary representation: " << s << std::endl;
    std::cout << "Enter a binary number: ";
    std::cin >> s;
    std::cout << "Decimal representation: " << s.to_ulong();
    return 0;
}