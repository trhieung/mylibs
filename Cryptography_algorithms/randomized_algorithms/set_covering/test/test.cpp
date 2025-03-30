#include "../core/set_covering.hpp"


int main(){
    unsigned int num_vec = 3, num_dim = 4;
    
    // Generate a matrix with values in the range [0, 10], verbose mode enabled
    void *matrix = set_covering::utils::gen_matrix(num_vec, num_dim, true, {0, 10});
    
    // Free allocated memory
    set_covering::utils::free_matrix(matrix);

    return 0;
}