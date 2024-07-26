#include <iostream>
#include <vector>

int findMax(std::vector<int> arr)
{
    int maxNum = arr[0];
    for (auto i : arr) {
        if (maxNum < i) {
            maxNum = i;
        } else {
            /* Do Nothing */
        }
    }
    return maxNum;
}

int main()
{
    std::vector<int> arr = { 1, 4, 21, 7, 3, 11, 5 };
    std::cout << findMax(arr);
    return 0;
}