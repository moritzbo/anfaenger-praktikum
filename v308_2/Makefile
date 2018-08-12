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

build/hysterese.pdf: python/hysterese.py header-matplotlib.tex matplotlibrc python/hysterese.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python python/hysterese.py

build/helmkombi2.pdf: python/helmkombi2.py python/helm2a.txt python/helm2i.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/helmkombi2.py
build/2AiZOOM.pdf: build/helmkombi2.pdf

build/helmkombi4.pdf: python/helmkombi4.py python/helm4a.txt python/helm4i.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/helmkombi4.py
build/4AiZOOM.pdf: build/helmkombi4.pdf

build/spulen.pdf: python/spulen.py python/spuleL.txt python/spuleK.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/spulen.py
build/spule_kurz.pdf: build/spulen.pdf

build/main.pdf: build/hysterese.pdf \
	build/helmkombi2.pdf \
	build/2AiZOOM.pdf \
	build/helmkombi4.pdf \
	build/4AiZOOM.pdf \
	build/spulen.pdf \
	build/spule_kurz.pdf

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
