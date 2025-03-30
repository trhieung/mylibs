
#include "johnson_lindenstrauss_export.hpp"
#include <iostream>
#include <vector>
#include <iomanip>

void local_check()
{
    std::cout << "local check!\n";
}
void print_ls(std::vector<unsigned int> ls)
{
    for (unsigned int i = 0; i < ls.size(); i++)
    {
        std::cout << std::setw(5) << ls[i] << " ";
    }
}

void myExport(unsigned int* arr, int size)
{
    std::vector<unsigned int> ls(arr, arr + size); 
    int n = ls.size() - 1;
    // std::cout << "Before sorting: ";
    // print_ls(ls);
    
    // Bubble Sort in C++
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n - 1; ++j) {
            if (ls[j] > ls[j + 1]) {
                std::swap(ls[j], ls[j + 1]);
            }
        }
    }

    // std::cout << "\nAfter sorting: ";
    // print_ls(ls);
}