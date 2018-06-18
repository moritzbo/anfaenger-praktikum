ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/main.pdf \
	build/leistung.pdf build/leistung.txt \
	build/mono.pdf\
	build/rechteck.pdf build/rechteck1.txt build/rechteck2.txt \
	build/sinus.pdf build/sinus1.txt build/sinus2.txt

build/mono.pdf: python/b.py python/daten/werte_b.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/b.py

build/leistung.pdf: python/c.py python/daten/werte_c.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/c.py
build/leistung.txt: build/leistung.pdf

build/rechteck.pdf: python/d.py python/daten/werte_d.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/d.py
build/rechteck1.txt: build/rechteck.pdf
build/rechteck2.txt: build/rechteck.pdf
build/sinus.pdf: build/rechteck.pdf
build/sinus1.txt: build/rechteck.pdf
build/sinus2.txt: build/rechteck.pdf

build/main.pdf: build/leistung.pdf build/leistung.txt \
			build/mono.pdf \
			build/rechteck.pdf build/rechteck1.txt build/rechteck2.txt \
			build/sinus.pdf build/sinus1.txt build/sinus2.txt

build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
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
