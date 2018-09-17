ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
	# Unix
	pwd := $$(pwd)
	translate = $1
else
	# Windows mit MSys2/Cygwin
	pwd := $$(cygpath -m "$$(pwd)")
	translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/ausgleichsgerade.pdf \
	build/rechnung.txt \
	build/berechnet.txt

build/ausgleichsgerade.pdf: linreg.py werte.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python linreg.py
build/rechnung.txt: build/ausgleichsgerade.pdf
build/berechnet.txt: build/ausgleichsgerade.pdf

build:
	mkdir -p build

clean:
	rm -rf build

.PHONY: all clean
