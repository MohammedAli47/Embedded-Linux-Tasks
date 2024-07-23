#include <iostream>

int main()
{
    int angle1, angle2, angle3;
    std::cout << "Enter 3 angles:" << std::endl;
    std::cin >> angle1 >> angle2 >> angle3;
    if (angle1 + angle2 + angle3 == 180) {
        if (angle1 == 90 || angle2 == 90 || angle3 == 90) {
            std::cout << "Angles form a right angle triangle";
        } else {
            std::cout << "Angles don't form a right angle triangle, but form a normal one";
        }

    } else {
        std::cout << "Angles don't form a triangle";
    }
    return 0;
}