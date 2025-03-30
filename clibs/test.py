
from myclibs import cpp_f_run

# Example Usage
so_path = "../Cryptography_algorithms/randomized_algorithms/johnson_lindenstrauss/build/Release/libs/johnson_lindenstrauss_export.so"
exported_functions = cpp_f_run.get_exported_functions(so_path)

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
