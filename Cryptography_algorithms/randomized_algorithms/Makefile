.PHONY: help
help:             	## Show the help.
	@echo "Usage: make <target>"
	@echo "----"
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep

.PHONY: create-module
create-module:     	## Create a new module (asks for name)
	@read -p "Project name? (provide the name of module): " module; \
	export module; \
	../config/initModule.sh "$$module"

