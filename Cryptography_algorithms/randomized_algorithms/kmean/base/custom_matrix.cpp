#include "custom_matrix.hpp"

cusMatrix::cusMatrix(const unsigned int &nums, const unsigned int &dims) : nums(nums), dims(dims), val(nullptr)
{
    if (nums > max_nums || dims > max_dims)
        throw std::invalid_argument("Matrix size exceeds allowed limits. (max nums = " +
                                    std::to_string(max_nums) + ", max dims = " +
                                    std::to_string(max_dims) + ")");

    val = new double[nums * dims];

    std::srand(static_cast<unsigned int>(std::time(nullptr)));
    std::generate(val, val + nums * dims, []()
                  { return static_cast<double>(std::rand()) / RAND_MAX; });
}

cusMatrix::~cusMatrix() { delete[] val; }

void cusMatrix::show() const
{
    if (!val)
    {
        std::cout << "Initialization failed: invalid matrix size.\n";
        return;
    }

    for (unsigned int i = 0; i < nums; ++i)
    {
        for (unsigned int j = 0; j < dims; ++j)
            std::cout << std::setw(8) << std::fixed << std::setprecision(4) << val[i * dims + j] << " ";
        std::cout << '\n';
    }
}

double *cusMatrix::getVal()
{
    return val;
}