# config/local.mk

# # tree
# <folder_name>
# ├── build
# |	|--Release
# |	|	|--libs
# |	|	|	|--core_obj -> include all objects in core folder
# |	|	|	|--test_obj -> include all objects in test folder
# |	|	|	|--<folder_name>_export.a -> static libs
# |	|	|	|--<folder_name>_export.so -> share libs
# |	|	|--exe
# |	|		|--test.exe -> only one main in this project for test!
# |	|
# |	|--Debug
# |	|	|--libs
# |	|	|	|--core_obj
# |	|	|	|--test_obj
# |	|	|--exe
# |			|--test.exe
# |
# ├── core
# │   ├── f1.cpp
# │   └── f1.hpp
# ├── <folder_name>_export.cpp
# ├── <folder_name>_export.hpp -> this export file will can include all the core and it obj link with their too, not including main
# ├── local.mk
# └── tests
#     ├── test.cpp
#     ├── unit1.cpp
#     └── unit1.hpp

# Project name
FOLDER_NAME = $(notdir $(CURDIR))
BUILD_DIR = build
RELEASE_DIR = $(BUILD_DIR)/Release
DEBUG_DIR = $(BUILD_DIR)/Debug

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -I. -fPIC
RELEASE_FLAGS = -O2
DEBUG_FLAGS = -g

# Source files
CORE_SRC = $(wildcard core/*.cpp)
CORE_OBJ = $(patsubst core/%.cpp,$(RELEASE_DIR)/libs/core_obj/%.o,$(CORE_SRC))
TEST_SRC = $(wildcard tests/*.cpp)
TEST_OBJ = $(patsubst tests/%.cpp,$(RELEASE_DIR)/libs/test_obj/%.o,$(TEST_SRC))
EXPORT_SRC = $(FOLDER_NAME)_export.cpp
EXPORT_OBJ = $(RELEASE_DIR)/libs/$(FOLDER_NAME)_export.o

# Targets
.PHONY: all release debug clean

all: release

release: CXXFLAGS += $(RELEASE_FLAGS)
release: $(RELEASE_DIR)/exe/test.exe

debug: CXXFLAGS += $(DEBUG_FLAGS)
debug: $(DEBUG_DIR)/exe/test.exe

# Compile core objects
$(RELEASE_DIR)/libs/core_obj/%.o: core/%.cpp | $(RELEASE_DIR)/libs/core_obj
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(DEBUG_DIR)/libs/core_obj/%.o: core/%.cpp | $(DEBUG_DIR)/libs/core_obj
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Compile test objects
$(RELEASE_DIR)/libs/test_obj/%.o: tests/%.cpp | $(RELEASE_DIR)/libs/test_obj
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(DEBUG_DIR)/libs/test_obj/%.o: tests/%.cpp | $(DEBUG_DIR)/libs/test_obj
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Compile export object
$(EXPORT_OBJ): $(EXPORT_SRC) | $(RELEASE_DIR)/libs
	$(CXX) $(CXXFLAGS) -c $< -o $@

# # Create static library
# $(RELEASE_DIR)/libs/$(FOLDER_NAME)_export.a: $(CORE_OBJ) $(EXPORT_OBJ)
# 	ar rcs $@ $^

# Create shared library
$(RELEASE_DIR)/libs/$(FOLDER_NAME)_export.so: $(CORE_OBJ) $(EXPORT_OBJ)
	$(CXX) -shared -fPIC -o $@ $^

# Link test executable
# # Using static
# $(RELEASE_DIR)/exe/test.exe: $(TEST_OBJ) $(RELEASE_DIR)/libs/$(FOLDER_NAME)_export.a | $(RELEASE_DIR)/exe
# 	$(CXX) $(CXXFLAGS) -o $@ $^

# $(DEBUG_DIR)/exe/test.exe: $(patsubst $(RELEASE_DIR)%, $(DEBUG_DIR)%,$(TEST_OBJ)) $(DEBUG_DIR)/libs/$(FOLDER_NAME)_export.a | $(DEBUG_DIR)/exe
# 	$(CXX) $(CXXFLAGS) -o $@ $^

# Using share
$(RELEASE_DIR)/exe/test.exe: $(TEST_OBJ) $(RELEASE_DIR)/libs/$(FOLDER_NAME)_export.so | $(RELEASE_DIR)/exe
	$(CXX) $(CXXFLAGS) -o $@ $^

$(DEBUG_DIR)/exe/test.exe: $(patsubst $(RELEASE_DIR)%, $(DEBUG_DIR)%,$(TEST_OBJ)) $(DEBUG_DIR)/libs/$(FOLDER_NAME)_export.so | $(DEBUG_DIR)/exe
	$(CXX) $(CXXFLAGS) -o $@ $^

# Create necessary directories
$(RELEASE_DIR)/libs/core_obj $(RELEASE_DIR)/libs/test_obj $(RELEASE_DIR)/libs $(RELEASE_DIR)/exe:
	mkdir -p $@

$(DEBUG_DIR)/libs/core_obj $(DEBUG_DIR)/libs/test_obj $(DEBUG_DIR)/libs $(DEBUG_DIR)/exe:
	mkdir -p $@

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)

