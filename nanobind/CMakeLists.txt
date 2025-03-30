cmake_minimum_required(VERSION 3.29)
project(nanobind_exp)

if (CMAKE_VERSION LESS 3.29)
    set(DEV_MODULE Development)
else()
    set(DEV_MODULE Development.Module)
endif()

find_package(Python 3.11 COMPONENTS Interpreter ${DEV_MODULE} REQUIRED)

if (NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "No build type set, set default to `Release`" FORCE)
    set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Release" "Debug" "MinSizeRel" "RelWithDebInfo")
endif()

# Find the 'nanobind' CMake directory
execute_process(
    COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE
    OUTPUT_VARIABLE nanobind_ROOT
)

find_package(nanobind CONFIG REQUIRED)

# Compile `my_extension` with `nanobind_add_module`.
# Note: `nanobind_add_module` resembles standard CMake commands like `add_executable()` and `add_library()`
# nanobind_add_module(my_ext my_ext.cpp)
nanobind_add_module(object_ownership object_ownership.cpp)
# Show all variables in CMake
# get_cmake_property(all_variables VARIABLES)
# foreach(var IN LISTS all_variables)
#     message(STATUS "CMake Variable: ${var} = ${${var}}")
# endforeach()
cmake_path(GET nanobind_ROOT PARENT_PATH nanobind_INCLUDE_DIRS)
set(nanobind_INCLUDE_DIRS ${nanobind_INCLUDE_DIRS}/include)
message(STATUS ${nanobind_INCLUDE_DIRS})
# target_include_directories(my_ext PRIVATE ${nanobind_INCLUDE_DIRS})