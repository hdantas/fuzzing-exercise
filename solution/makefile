# Inspired by Mozilla
# https://wiki.mozilla.org/Security/Fuzzing/Peach

FUZZ_ROOT=/Users/nuno
PYTHON=python2.7

PEACH_PY=$(FUZZ_ROOT)/Downloads/Peach-2.3.9-src/peach.py

PEACH_ARGS=
PEACH_ONE=-1
PEACH_PARSE=-t
PEACH_DEBUG=--debug

PEACH_XML=$(FUZZ_ROOT)/repos/twente-exercise/solution/solution.xml

all: fuzz

one: message
	$(PYTHON) $(PEACH_PY) $(PEACH_ONE) $(PEACH_XML)

parse: message
	$(PYTHON) $(PEACH_PY) $(PEACH_PARSE) $(PEACH_XML)

fuzz: message
	$(PYTHON) $(PEACH_PY) $(PEACH_ARGS) $(PEACH_XML)

#####################################


message:
	@echo "Running command: $(PYTHON) $(PEACH_PY) $(PEACH_ARGS) $(PEACH_XML)"

log-message:
	@echo "Logging output to $(PEACH_OUTPUT_LOG)"
	@echo "Running command: $(PYTHON) $(PEACH_PY) $(PEACH_ARGS) $(PEACH_XML) >$(PEACH_OUTPUT_LOG) 2>1"
