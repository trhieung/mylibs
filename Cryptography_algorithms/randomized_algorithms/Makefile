.PHONY: help
help:             	## Show the help.
	@echo "Usage: make <target>"
	@echo "----"
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep


# .PHONY: create-module
# create-module:     	## Create a new module (asks for name)
# 	@read -p "Project name? (provide the name of module): " module; \
# 	mkdir -p "$${module}" "$${module}/core" "$${module}/tests"; \
# 	echo "[+] Export definitions for $${module} and $${module}/core" ; \
# 	cp ../config/template_export.hpp "$${module}/$${module}_export.hpp"; \
# 	cp ../config/template_export.hpp "$${module}/$${module}_export.hpp"; \
# 	echo "// #pragma once" > "$${module}/core/$${module}.hpp"; \
# 	echo "[+] Export implementation for $${module} and $${module}/core"; \
# 	echo "#include \"core/$${module}.hpp\"\n#include \"$${module}_export.hpp\"" > "$${module}/$${module}_export.cpp"; \
# 	echo "#include \"$${module}.hpp\"" > "$${module}/core/$${module}.cpp"; \
# 	cp ../config/template_local.mk ./$${module}/Makefile
# 	echo "Module $${module} created successfully!"


.PHONY: create-module
create-module:     	## Create a new module (asks for name)
	@read -p "Project name? (provide the name of module): " module; \
	export module; \
	../config/initModule.sh "$$module"

