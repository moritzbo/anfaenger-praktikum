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
	build/totzeit.txt \
	build/zzz.txt

build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=batchmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
