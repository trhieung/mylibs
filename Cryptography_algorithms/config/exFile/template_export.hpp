#ifndef __TEMPLATE_EXPORT_H__
#define __TEMPLATE_EXPORT_H__

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

#endif  // __TEMPLATE_EXPORT_H__
