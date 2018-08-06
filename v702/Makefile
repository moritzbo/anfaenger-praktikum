ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  pwd := $$(pwd)
  translate = $1
endif

all: build/main.pdf

build/Indiumfit.pdf: python/Indium.py python/indium.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/Indium.py
build/Indiumwerte.pdf: build/Indiumfit.pdf
build/indium.txt: build/Indiumfit.pdf

build/Rhodium.pdf: python/rhodium.txt python/Rhodium.py header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/Rhodium.py
build/shortfit.pdf: build/Rhodium.pdf

# hier Python-Skripte:
# build/25a.pdf: python/raumladung.py python/25a.txt python/nano.txt header-matplotlib.tex matplotlibrc | build
# 	TEXINPUTS="$(pwd):" python python/raumladung.py
# hier alle txt und pdf abhängigkeiten rein

build/main.pdf: build/Indiumfit.pdf \
	build/Indiumwerte.pdf \
	build/indium.txt \
	build/Rhodium.pdf \
	build/shortfit.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex


build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
