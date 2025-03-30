#ifndef __kmean_export_h__
#define __kmean_export_h__

// Include core header here!
// #include "core/template.hpp"

// Setting for export with symbol file only
void local_check();

// Setting for export functions
#ifdef __cplusplus
extern "C" {
#endif

// export function here!
//------------------------------


void myExport();


//------------------------------
#ifdef __cplusplus
}
#endif

#endif  // __kmean_export_h__
