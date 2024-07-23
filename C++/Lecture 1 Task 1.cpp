#include <iomanip>
#include <iostream>


int main()
{
    std::cout << "+------+-------+" << std::endl;
    std::cout << "| Char | ASCII |" << std::endl;
    std::cout << "+------+-------+" << std::endl;
    for (int i = 32; i <= 126; i++) {
        std::cout << "| " << std::setw(3) << char(i) << "  |  " << std::setw(3) << i << "  |" << std::endl;
    }
	std::cout << "+------+-------+" << std::endl;
    return 0;
}