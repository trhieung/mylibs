#include "kmean.hpp"

kmean::kmean(const unsigned short &nCluster, const unsigned int &nSample, const unsigned int &dims, const double *val)
    : nClusters(nCluster), nSample(nSample), dims(dims), centroids(nullptr), belongs(nullptr), val(nullptr)
{
    if (nCluster > maxClusters)
        throw std::invalid_argument("Cluster size exceeds allowed limits. (max " + std::to_string(maxClusters) + ")");

    belongs = new unsigned char[nSample](); // Zero-initialized

    centroids = new unsigned int[nCluster];

    // Seed random number generator (only once per program execution)
    static bool seeded = false;
    if (!seeded)
    {
        std::srand(static_cast<unsigned int>(std::time(nullptr)));
        seeded = true;
    }

    // Assign random sample indices to centroids
    for (unsigned short i = 0; i < nCluster; i++)
    {
        centroids[i] = std::rand() % nSample; // Random index in range [0, nSample-1]
    }

    if (val) // Ensure input is not null before allocating memory
    {
        this->val = new double[dims * nSample];
        std::memcpy(this->val, val, dims * nSample * sizeof(double)); // Copy input data
    }
}

kmean::~kmean()
{
    delete[] centroids;
    delete[] belongs;
    delete[] val;
}

void kmean::makeConvergrence()
{
    /*
        att     |   sz              |   meaning
    - val       | dims * nSample    | dims = 2, sample = 3 [[1, 1], [1, 2], [3, 1]]
    - centroids | nCluster          | centroids[i] = centor of cluster with id i
    - belongs   | nSample           | belongs[i] indicate the sample[i]
    */
   
}