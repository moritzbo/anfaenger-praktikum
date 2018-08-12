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

build/lange-spule.pdf: python/plots.py python/daten/lange-spule.txt python/daten/kurze-spule.txt python/daten/hysterese.txt python/daten/helmholtz-7.txt python/daten/helmholtz-8.txt python/daten/helmholtz-9.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/plots.py
build/kurze-spule.pdf: build/lange-spule.pdf
build/hysterese.pdf: build/lange-spule.pdf

build/main.pdf: build/fehler.txt \
	build/lange-spule.pdf \
	build/kurze-spule.pdf \
	build/hysterese.pdf

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
