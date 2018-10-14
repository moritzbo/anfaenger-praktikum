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

build/Indiumfit.pdf: python/Indium.py python/indium.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/Indium.py
build/Indiumwerte.pdf: build/Indiumfit.pdf
build/indium.txt: build/Indiumfit.pdf

build/Rhodium.pdf: python/rhodium.txt python/Rhodium.py header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/Rhodium.py
build/shortfit.pdf: build/Rhodium.pdf

build/main.pdf: build/Indiumfit.pdf \
	build/Indiumwerte.pdf \
	build/indium.txt \
	build/Rhodium.pdf \
	build/shortfit.pdf

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
