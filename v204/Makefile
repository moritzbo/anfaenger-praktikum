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

build/statisch.pdf: python/statisch.py python/statisch.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/statisch.py
build/statisch-unterschied.pdf: build/statisch.pdf
build/statisch.txt: build/statisch.pdf
build/waermestrom.txt: build/statisch.pdf

build/messing.pdf: python/dynamisch.py python/dynamisch.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/dynamisch.py
build/messingminmax.txt: build/messing.pdf
build/aluminium.pdf: build/messing.pdf
build/aluminiumminmax.txt: build/messing.pdf

build/edelstahl.pdf: python/edelstahl.py python/edelstahl.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/edelstahl.py
build/edelstahlmminmax.txt: build/edelstahl.pdf

build/main.pdf:build/statisch.pdf \
	build/statisch-unterschied.pdf \
	build/statisch.txt \
	build/waermestrom.txt \
	build/messing.pdf \
	build/messingminmax.txt \
	build/aluminium.pdf \
	build/aluminiumminmax.txt \
	build/edelstahl.pdf \
	build/edelstahlmminmax.txt

build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
    BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=batchmode \
	  --halt-on-error \
	  --time \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
