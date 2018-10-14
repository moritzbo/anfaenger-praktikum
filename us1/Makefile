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

build/fehler.txt: python/fehler.py | build
	TEXINPUTS="$(pwd):" python python/fehler.py

build/acrylschall.pdf: python/mess_schall_daempf.py python/daten/daempfung.txt python/daten/programm/Messung-1.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/mess_schall_daempf.py
build/absorption.txt: build/acrylschall.pdf

build/daempfefit.pdf: python/daempfen.py python/daten/daempfung.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/daempfen.py
build/daempfwerte.txt: build/daempfefit.pdf

build/echopuls.pdf: python/daten/daempfung.txt header-matplotlib.tex matplotlibrc python/echopuls.py | build
	TEXINPUTS="$(pwd):" python python/echopuls.py
build/echopuls.txt: build/echopuls.pdf

build/durchschall.pdf: python/daten/durchschallung.txt header-matplotlib.tex matplotlibrc python/durchschall.py | build
	TEXINPUTS="$(pwd):" python python/durchschall.py
build/durchschall.txt: build/durchschall.pdf

build/fft.pdf: python/spektral.py python/fftwerte.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/spektral.py

build/auge1.pdf: python/auge1.py python/daten/programm/auge1.Txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/auge1.py
build/augwert.txt: build/auge1.pdf

build/doppelblatt.pdf: python/doppelblatt.py python/daten/programm/doppelblattzylindermessung.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/doppelblatt.py

build/main.pdf: build/fehler.txt \
	build/acrylschall.pdf \
	build/absorption.txt \
	build/daempfefit.pdf \
	build/daempfwerte.txt \
	build/echopuls.pdf \
	build/echopuls.txt \
	build/durchschall.pdf \
	build/durchschall.txt \
	build/fft.pdf \
	build/auge1.pdf \
	build/augwert.txt \
	build/doppelblatt.pdf

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
