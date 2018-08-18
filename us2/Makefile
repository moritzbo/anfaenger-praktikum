ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
	# Unix
	pwd := $$(pwd)
	translate = $1
else
	# Windows mit MSys2/Cygwin
	pwd := $$(cygpath -m "$$(pwd)")
	translate = $(shell echo '$1' | sed 's/:/;/g')
endif

# Am Ende soll das Protokoll stehen
all: build/main.pdf

# hier stehen die Python-Dateien
build/scan.txt: python/scan.py python/daten/bohrungen.txt | build
	TEXINPUTS="$(pwd):" python python/scan.py

build/herz.pdf: python/herz.py python/daten/herzwelle.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(pwd):" python python/herz.py

# Alle für das Protokoll benötigten Dateien
build/main.pdf: build/scan.txt \
	build/herz.pdf

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
