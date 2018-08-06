ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  pwd := $$(pwd)
  translate = $1
endif

all: build/main.pdf

# hier Python-Skripte:
build/kennlinie.pdf: python/kennlinie.py python/2a.txt python/21a.txt python/22-23-24a.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/kennlinie.py

build/kennlinientemperatur.txt: build/kennlinie.pdf

build/kennliniendaten.txt: build/kennlinie.pdf

build/25a.pdf: python/raumladung.py python/25a.txt python/nano.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/raumladung.py

build/nano.txt: build/25a.pdf
# hier alle txt und pdf abhängigkeiten rein

build/main.pdf: build/kennlinie.pdf \
	build/kennlinientemperatur.txt \
	build/kennliniendaten.txt \
	build/25a.pdf \
	build/nano.txt

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
