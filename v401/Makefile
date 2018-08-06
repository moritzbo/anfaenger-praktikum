all: build/main.pdf

# hier Python-Skripte:
build/vakuum.txt: python/rechnung.py python/vakuum.txt python/wellenlaenge.txt | build
	python python/rechnung.py
build/wellenlaenge.txt: build/vakuum.txt

#	hier alle txt und pdf abhängigkeiten rein
build/main.pdf: build/vakuum.txt build/wellenlaenge.txt
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
