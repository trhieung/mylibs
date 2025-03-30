// #pragma once
#ifndef __CUSTOM_MATRIX_HPP__
#define __CUSTOM_MATRIX_HPP__

#include <iostream>
#include <iomanip>
#include <cstdlib> // for rand()
#include <ctime>   // for seeding rand()
#include <algorithm>
#include <stdexcept>
#include <string>


class cusMatrix
{
protected:
    unsigned int nums;
    unsigned int dims;
    double *val;

    const unsigned int max_nums = 1<<10;
    const unsigned int max_dims = 1<<4;

public:
    cusMatrix(const unsigned int &nums, const unsigned int &dims);
    ~cusMatrix();

    void show() const;
    double* getVal();
};
#endif // __CUSTOM_MATRIX_HPP__