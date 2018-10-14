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

build/Energieverteilung.pdf: python/EZimm.py header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/EZimm.py

build/intE-153.pdf: python/Ehot.py header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/Ehot.py

build/main.pdf: build/Energieverteilung.pdf \
	build/intE-153.pdf

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
