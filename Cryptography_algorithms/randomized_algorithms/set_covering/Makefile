ModuleDir = .
ProjectDir = ..
ConfigDir = ../../config

include $(ConfigDir)/local.mk

# Additional custom rules for this project
all: check

check: release
run: release 
	./build/Release/exe/test.exe