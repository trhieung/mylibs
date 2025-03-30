#include <iostream>
#include "unitTest.hpp"
#include "../base/custom_matrix.hpp"

int main()
{
    std::cout << "Hi from main\n";
    cusMatrix x = cusMatrix(10, 2);
    x.show();
    std::cout << "End from main\n";
    return 0;
}