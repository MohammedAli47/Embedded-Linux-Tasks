#include <iostream>

int main()
{
    char c;
    std::cout << "Enter a character: ";
    std::cin >> c;
    switch (c) {
    case 'a':
    case 'A':
    case 'e':
    case 'E':
    case 'i':
    case 'I':
    case 'o':
    case 'O':
    case 'u':
    case 'U':
        std::cout << "Character is a vowel";
        break;
    default:
        std::cout << "Character is not a vowel";
        break;
    }
    return 0;
}