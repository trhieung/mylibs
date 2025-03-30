#ifndef __JOHNSON_LINDENTRAUSS_EXPORT_H__
#define __JOHNSON_LINDENTRAUSS_EXPORT_H__

// Include core header here!
#include "core/f1.hpp"
#include <vector>
#include <iostream>

void local_check();
#ifdef __cplusplus
extern "C" {
#endif

// export function here!
//------------------------------


void myExport(unsigned int* arr, int size);


//------------------------------
#ifdef __cplusplus
}
#endif

#endif  // __JOHNSON_LINDENTRAUSS_EXPORT_H__
