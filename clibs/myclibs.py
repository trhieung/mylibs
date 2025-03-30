import ctypes
from functools import wraps
from elftools.elf.elffile import ELFFile

from nanobind import *

class cpp_f_run:
    def __init__(self, so_file):
        self.lib = ctypes.CDLL(so_file)

    @staticmethod
    def session(name, argtypes=None, restype=None):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args):
                c_func = getattr(self.lib, name, None)
                if c_func is None:
                    raise AttributeError(f"Function '{name}' not found in the shared library.")

                if argtypes:
                    c_func.argtypes = argtypes
                if restype:
                    c_func.restype = restype

                return c_func(*args)
            return wrapper
        return decorator
    
    
    # Function to get exported functions from .so file
    @staticmethod
    def get_exported_functions(so_file):
        exported_funcs = []
        with open(so_file, "rb") as f:
            elf = ELFFile(f)
            symtab = elf.get_section_by_name('.dynsym')  # Get dynamic symbol table

            if not symtab:
                print("No dynamic symbol table found.")
                return []

            for sym in symtab.iter_symbols():
                if (
                    sym['st_info']['type'] == 'STT_FUNC' and 
                    sym['st_info']['bind'] == 'STB_GLOBAL' and 
                    not sym.name.startswith('_')  # Ignore functions starting with '_'
                ):
                    exported_funcs.append(sym.name)

        return exported_funcs

import ctypes
import numpy as np
from time import time

# Path to the shared library
so_path = "../Cryptography_algorithms/randomized_algorithms/johnson_lindenstrauss/build/Release/libs/johnson_lindenstrauss_export.so"

# Load the shared library
lib = ctypes.CDLL(so_path)

# Define the function prototype
lib.myExport.argtypes = [ctypes.POINTER(ctypes.c_uint), ctypes.c_size_t]
lib.myExport.restype = None  # Assuming it doesn't return a value

# Prepare the input array
values = np.arange(10000, -1, -1, dtype=np.uint32)  # Generates [10000, 9999, ..., 0]
values_ctypes = values.ctypes.data_as(ctypes.POINTER(ctypes.c_uint))

# Call the function
st = time()
lib.myExport(values_ctypes, len(values))
print(time()-st)

# Print modified values (if `myExport` modifies the array)
# print("Modified values:", values.tolist())
