ModuleDir = .
ProjectDir = ..
ConfigDir = ../../config

# Set default value for isBase if not overridden
isBase ?= true

ifeq ($(isBase), true)
    include $(ConfigDir)/localWithBase.mk
else
    include $(ConfigDir)/local.mk
endif

# Additional custom rules for this project
all: check

check: release # can replace the release by debug

run: release 
	./build/Release/exe/test.exe
