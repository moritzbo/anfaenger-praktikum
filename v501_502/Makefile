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

build/fitefeld.pdf: python/ausgleich.py python/D0.txt python/D1_D2.txt python/D4_D5.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/ausgleich.py
build/empfindlichkeit.pdf: build/fitefeld.pdf

build/b_feld1.pdf: python/linreg502.py python/502werte.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/linreg502.py

build/stehwelle.txt: python/stehwelle.py python/stehwelle.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/stehwelle.py

build/main.pdf: build/fitefeld.pdf \
		build/empfindlichkeit.pdf \
		build/b_feld1.pdf \
		build/stehwelle.txt

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
