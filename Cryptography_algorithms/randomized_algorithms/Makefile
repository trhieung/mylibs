.PHONY: help
help:             	## Show the help.
	@echo "Usage: make <target>"
	@echo "----"
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep


.PHONY: create-module
create-module:     	## Create a new module (asks for name)
	@read -p "Project name? (provide the name of module): " module; \
	mkdir -p "$${module}" "$${module}/core" "$${module}/tests"; \
	echo "[+] Export definitions for $${module}"; \
	echo "// #pragma once" > "$${module}/$${module}_export.h"; \
	echo "[+] Export implementation for $${module}"; \
	echo "// #pragma once" > "$${module}/$${module}_export.c"; \
	echo "Module $${module} created successfully!"

