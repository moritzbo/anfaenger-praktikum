ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
	# Unix
	pwd := $$(pwd)
	translate = $1
else
	# Windows mit MSys2/Cygwin
	pwd := $$(cygpath -m "$$(pwd)")
	translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/main.pdf

build/vakuum.txt: python/rechnung.py python/vakuum.txt python/wellenlaenge.txt | build
	python python/rechnung.py
build/wellenlaenge.txt: build/vakuum.txt

build/main.pdf: build/vakuum.txt \
	build/wellenlaenge.txt

build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=batchmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
