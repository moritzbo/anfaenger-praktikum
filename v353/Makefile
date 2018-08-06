ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif


# unter all kommen alle Dateien die durch das Makefile erstellt werden
all: build/main.pdf build/linreg_a.pdf build/werte_a.txt build/phasenplot.pdf

#  hier Python-Skripte: falls 2 Dateien in einem Script erstellt werden:
# build/linreg_a.txt: build/linreg_a.pdf | build

build/linreg_a.pdf: python/script.py python/daten/werte_a.txt python/daten/werte_b_c.txt header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python python/script.py

build/werte_a.txt: build/linreg_a.pdf
build/phasenplot.pdf: build/linreg_a.pdf
build/phase.txt: build/linreg_a.pdf
build/amplitudenplot.pdf: build/linreg_a.pdf
build/amplitude.txt: build/linreg_a.pdf
build/polarplot.pdf: build/linreg_a.pdf
build/polar.txt: build/linreg_a.pdf

# hier alle build/dateien.endung die für main.tex gebraucht werden
build/main.pdf: build/linreg_a.pdf build/werte_a.txt build/phasenplot.pdf build/phase.txt build/amplitudenplot.pdf build/amplitude.txt build/polarplot.pdf build/polar.txt
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
