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

build/einzelspalt1.pdf: python/rechnungEinzel.py python/einzelspalt.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/rechnungEinzel.py

build/doppelspalt1_1.pdf: python/rechnungDoppel1.py python/doppelspalt1.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/rechnungDoppel1.py

build/doppelspalt2_1.pdf: python/rechnungDoppel2.py python/doppelspalt2.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/rechnungDoppel2.py

build/main.pdf: build/einzelspalt1.pdf \
	build/doppelspalt1_1.pdf \
	build/doppelspalt2_1.pdf

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
