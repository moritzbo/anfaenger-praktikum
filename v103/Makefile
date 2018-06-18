ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
	DETECTED = Windows
endif

all: build/main.pdf

build/rundeinseitig.pdf: python/linreg.py matplotlibrc header-matplotlib.tex python/stange1eckig.txt python/stange1rund.txt python/stange2.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/linreg.py
build/quadrateinseitig.pdf: build/rundeinseitig.pdf
build/quadrat_zweiseitig_rechts.pdf: build/rundeinseitig.pdf
build/quadrat_zweiseitig_links.pdf: build/rundeinseitig.pdf

build/main.pdf: build/rundeinseitig.pdf \
	build/quadrateinseitig.pdf \
	build/quadrat_zweiseitig_rechts.pdf \
	build/quadrat_zweiseitig_links.pdf

build/main.pdf: FORCE | build
ifneq ($(DETECTED),Windows)
		TEXINPUTS=.//:build: \
		BIBINPUTS=.//:build: \
		max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex
else
		TEXINPUTS=build; \
		BIBINPUTS=build; \
		max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex
endif

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
