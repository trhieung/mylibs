#include <nanobind/nanobind.h>
// #include <nanobind/stl/unique_ptr.h>
#include <nanobind/stl/bind_vector.h>
#include <chrono>
#include <iostream>
using VectorInt = std::vector<int>;
using namespace std::chrono;

void sort(VectorInt &vec) {
    int sze = vec.size();
    auto st = high_resolution_clock::now();
    for (int i = 0; i < sze - 1; ++i) {
        for (int j = 0; j < sze - 1 - i; ++j) {
            if (vec[j] > vec[j + 1]) {
                std::swap(vec[j], vec[j + 1]);
            }
        }
    }
    auto stop = high_resolution_clock::now();
    std::cout << duration_cast<milliseconds>(stop - st).count() << std::endl;
}

namespace nb = nanobind;
NB_MODULE(object_ownership, m){
    // object 
    nb::bind_vector<VectorInt>(m, "VectorInt");
    m.def("sort", &sort);
}