import ctypes
from functools import wraps
from elftools.elf.elffile import ELFFile

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


# Example Usage
so_path = "../Cryptography_algorithms/randomized_algorithms/johnson_lindenstrauss/build/Release/libs/johnson_lindenstrauss_export.so"
exported_functions = get_exported_functions(so_path)

# Check if functions are exported
if not exported_functions:
    print("No functions exported!")
else:
    print("Exported Functions:", exported_functions)

    # Load the shared library
    cpp_lib = cpp_f_run(so_path)

    # Example function with no arguments and void return (e.g., void hello_world();)
    @cpp_lib.session(name=exported_functions[0], argtypes=[], restype=None)
    def session_template():
        pass

    # Call the function
    session_template()
