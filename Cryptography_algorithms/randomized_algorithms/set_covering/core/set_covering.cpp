#include "set_covering.hpp"

#include <iostream>
#include <iomanip>
#include <vector>
#include <random>

// Proper loop structure for printing
void set_covering::utils::print_matrix(void *matrix, const unsigned int &num_vec, const unsigned int &num_dim)
{
    std::cout << "[+] Your matrix:\n";
    auto *mat = static_cast<unsigned int *>(matrix);

    for (auto i = 0U; i < num_vec; ++i) // Loop correctly over indices
    {
        for (auto j = 0U; j < num_dim; ++j)
        {
            std::cout << std::setw(5) << mat[i * num_dim + j] << " ";
        }
        std::cout << std::endl;
    }
}

// Generate a matrix with random values
void *set_covering::utils::gen_matrix(const unsigned int &num_vec,
                                      const unsigned int &num_dim,
                                      const bool& verbose,
                                      const std::pair<unsigned int, unsigned int> range_val) // range of values
{
    auto *_matrix = new unsigned int[num_vec * num_dim];

    // Fix: Use a proper seed for randomness
    static std::random_device rd;
    static std::mt19937 gen(rd());  // Seed only once globally
    std::uniform_int_distribution<unsigned int> dist(range_val.first, range_val.second);

    // Fill the matrix with random values
    for (auto i = 0U; i < num_vec * num_dim; ++i)
    {
        _matrix[i] = dist(gen);
    }

    if (verbose)
    {
        print_matrix(_matrix, num_vec, num_dim);
    }

    return static_cast<void *>(_matrix);
}

// Free allocated memory
void set_covering::utils::free_matrix(void *matrix)
{
    delete[] static_cast<unsigned int *>(matrix);
}
