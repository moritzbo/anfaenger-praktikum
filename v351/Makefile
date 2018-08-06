ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif


all: build/v351.pdf build/recht.pdf build/rechteck.txt build/rechteckanalyse.pdf build/dreieck.pdf build/dreieck.txt build/dreieckanalyse.pdf build/saege.pdf build/saegezahn.txt build/saegezahnanalyse.pdf
# hier Python-Skripte:
build/recht.pdf: python/skizzen.py header351-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/skizzen.py

build/dreieck.pdf: build/recht.pdf | build

build/saege.pdf: build/recht.pdf | build


build/dreieck.txt: python/dreieck.py python/dreieckanalyse.txt header351-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/dreieck.py

build/dreieckanalyse.pdf: build/dreieck.txt | build

build/rechteck.txt: python/rechteck.py python/rechteckanalyse.txt header351-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/rechteck.py

build/rechteckanalyse.pdf: build/rechteck.txt | build

build/saegezahn.txt: python/saegezahn.py python/saegezahnanalyse.txt header351-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/saegezahn.py

build/saegezahnanalyse.pdf: build/saegezahn.txt | build
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/v351.pdf:build/recht.pdf build/rechteck.txt build/rechteckanalyse.pdf build/dreieck.pdf build/dreieck.txt build/dreieckanalyse.pdf build/saege.pdf build/saegezahn.txt build/saegezahnanalyse.pdf

build/v351.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v351.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
