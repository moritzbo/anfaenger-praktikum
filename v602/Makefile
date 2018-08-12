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

build/vorbereitung.txt: python/vorbereitung.py | build
	TEXINPUTS="$(pwd):" python python/vorbereitung.py

build/bragg.pdf: python/bragg.txt python/bragg.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(pwd):" python python/bragg.py

build/emission.pdf: python/emission.txt python/emission.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(pwd):" python python/emission.py
build/emissionlog.pdf: build/emission.pdf

build/brom.pdf: python/brom.txt python/absorption.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(pwd):" python python/absorption.py
build/strontium.pdf: build/brom.pdf
build/zink.pdf: build/brom.pdf
build/zirkonium.pdf: build/brom.pdf
build/quecksilber.pdf: build/brom.pdf
build/absorption.txt: build/brom.pdf
build/ekphik.txt: build/brom.pdf

build/main.pdf: build/vorbereitung.txt \
	build/bragg.pdf \
	build/emission.pdf \
	build/emissionlog.pdf \
	build/brom.pdf \
	build/strontium.pdf \
	build/zink.pdf \
	build/zirkonium.pdf \
	build/quecksilber.pdf \
	build/absorption.txt \
	build/ekphik.txt

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
