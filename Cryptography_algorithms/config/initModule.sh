#!/bin/sh
module="$1"

# Validate input
if [ -z "$module" ]; then
    echo "Error: Module name is required."
    exit 1
fi

# Create module folder
mkdir -p "$module/core" "$module/base" "$module/test"
echo "[+] Setup make file for runnig"
cp ../config/template_local.mk "$module/Makefile"

# Create & init base folder
echo "[+] Export definitions for $module/base"
echo "// #pragma once" > "$module/base/b1.hpp"
echo "[+] Export implementation for $module/base"
echo "#include \"b1.hpp\"" > "$module/base/b1.cpp"

# Create & init core folder
echo "[+] Export definitions for $module/core"
echo "// #pragma once" > "$module/core/$module.hpp"
echo "[+] Export implementation for $module/core"
echo "#include \"$module.hpp\"" > "$module/core/$module.cpp"

# Create & init test folder
echo "[+] Setup default test"
cp ../config/exFile/test.cpp "$module/test/"
cp ../config/exFile/unitTest.hpp "$module/test/"
cp ../config/exFile/unitTest.cpp "$module/test/"

# Create & init export functions
echo "[+] Export definitions for $module"
cp ../config/exFile/template_export.hpp "$module/${module}_export.hpp"
cp ../config/exFile/template_export.cpp "$module/${module}_export.cpp"
sed -i "s/__TEMPLATE_EXPORT_H__/__${module}_export_h__/g" "$module/${module}_export.hpp"
sed -i "s/template_export.hpp/${module}_export.hpp/g" "$module/${module}_export.cpp"


echo "Module $module created successfully!"
