ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  pwd := $$(pwd)
  translate = $1
endif

all: build/main.pdf \
	build/zzz.txt

# hier Python-Skripte:
# build/25a.pdf: python/raumladung.py python/25a.txt python/nano.txt header-matplotlib.tex matplotlibrc | build
# 	TEXINPUTS="$(pwd):" python python/raumladung.py
# hier alle txt und pdf abhängigkeiten rein

build/impulse.pdf: python/impulse.py python/daten/impulse.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/impulse.py
build/impulse.txt: build/impulse.pdf
build/ladung.pdf: build/impulse.pdf

build/nachentladung.txt: python/nachentladung.py python/daten/nachentladung.txt
	TEXINPUTS="$(pwd):" python python/nachentladung.py

build/totzeit.txt: python/totzeit.py python/daten/totzeit.txt
	TEXINPUTS="$(pwd):" python python/totzeit.py

build/zzz.txt: python/fehler.py
	TEXINPUTS="$(pwd):" python python/fehler.py

build/main.pdf: build/impulse.pdf \
	build/impulse.txt \
	build/ladung.pdf \
	build/nachentladung.txt \
	build/totzeit.txt

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
