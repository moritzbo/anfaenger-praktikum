ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  pwd := $$(pwd)
  translate = $1
endif

all: build/main.pdf

build/Energieverteilung.pdf: python/EZimm.py header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/EZimm.py

build/intE-153.pdf: python/Ehot.py header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/Ehot.py
# hier Python-Skripte:
# build/25a.pdf: python/raumladung.py python/25a.txt python/nano.txt header-matplotlib.tex matplotlibrc | build
# 	TEXINPUTS="$(pwd):" python python/raumladung.py

# hier alle txt und pdf abhängigkeiten rein

build/main.pdf: build/Energieverteilung.pdf build/intE-153.pdf

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
