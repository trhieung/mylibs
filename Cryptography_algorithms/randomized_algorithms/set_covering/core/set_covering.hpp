// #pragma once
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <vector>
#include <unordered_map>
#include <string>
#include <unordered_set>

namespace set_covering
{
    class utils
    {
    public:
        // static method/function in class
        static void print_matrix(void *matrix, const unsigned int &num_vec, const unsigned int &num_dim);

        // static method/function in class
        static void *gen_matrix(const unsigned int &num_vec,
                                const unsigned int &num_dim,
                                const bool &verbose = false,
                                const std::pair<unsigned int, unsigned int> range_val = {0, 1}); // range of value

        // static method to free allocated memory
        static void free_matrix(void *matrix);
    };

    void find(const unsigned int &num_vec,
              const unsigned int &num_dim,
              void *matrix, 
              std::vector<int> cost)
    {
        
    }
}
