// #pragma once
#ifndef __KMEAN_HPP__
#define __KMEAN_HPP__

#include <stdexcept>
#include <string>
#include <algorithm>
#include <cstring> // For std::memcpy
#include <cstdlib>  // For std::rand(), std::srand()
#include <ctime>    // For std::time()

class kmean
{
private:
    unsigned short nClusters;
    unsigned int nSample;
    unsigned int dims;
    unsigned int *centroids;
    unsigned char *belongs;
    double *val;

    static constexpr unsigned short maxClusters = 8;

public:
    kmean(const unsigned short &nCluster, const unsigned int &nSample, const unsigned int &dims, const double *val);
    ~kmean();

    void makeConvergrence();
};

#endif // __KMEAN_HPP__
