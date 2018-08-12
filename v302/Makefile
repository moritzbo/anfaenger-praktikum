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

build/fehler.txt: python/fehler.py  | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/fehler.py

build/wert12.txt: python/mittelwert-widerstand.py  | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/mittelwert-widerstand.py
build/wert13.txt: build/wert12.txt

build/wert1.txt: python/mittelwert-kondensator.py  | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/mittelwert-kondensator.py
build/wert3.txt: build/wert1.txt
build/wert8.txt: build/wert1.txt

build/wert17a.txt: python/mittelwert-spule.py | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/mittelwert-spule.py
build/wert17b.txt: build/wert17a.txt

build/frequenz.pdf: python/frequenz.py python/werte-e.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/frequenz.py
build/frequenz.txt: build/frequenz.pdf
build/frequenz-klein.pdf: build/frequenz.pdf

build/main.pdf:	build/fehler.txt \
	build/wert12.txt \
	build/wert13.txt \
	build/wert1.txt \
	build/wert3.txt build/wert8.txt \
	build/wert17a.txt \
	build/wert17b.txt \
	build/frequenz.pdf \
	build/frequenz.txt \
	build/frequenz-klein.txt

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
