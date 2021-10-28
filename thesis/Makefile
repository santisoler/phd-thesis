# The name of the main .tex file to build.
THESIS = thesis
# List other .tex needed files
REFERENCES = references.bib
TEX_FILES = $(wildcard *.tex chapters/*.tex)
TEX_STYLES = $(wildcard *.sty *.bst)
FIGURES = $(wildcard figs/* figs/*/*)
PYTHON_EXAMPLES = $(wildcard fatiando-examples/*.py)
SOURCE_FILES = $(REFERENCES) $(TEX_FILES) $(TEX_STYLES) $(FIGURES) $(PYTHON_EXAMPLES)
# Folder where output will be placed
OUTDIR = _output
CHAPTERS_DIR = $(OUTDIR)/chapters
# Name of the output file
PDF = $(OUTDIR)/$(THESIS).pdf

LATEX_COMPILER = latexmk
LATEX_FLAGS = -pdf -outdir=$(OUTDIR)
LATEXMK_RC = .latexmkrc
PDFVIEWER = xdg-open

.PHONY: all help live clean word-count show bibsort live


all: $(PDF)

help:
	@echo "Commands:"
	@echo ""
	@echo "  all         build a PDF version of the thesis"
	@echo "  live        build and show the thesis with continuosly update"
	@echo "  show        opens the PDF with your favourite reader"
	@echo "  bibsort     autosort the BibTeX file alphabetically"
	@echo "  word-count  counts the number of words, figures, etc."
	@echo "  clean       clean up build and generated files"
	@echo ""

clean:
	rm -rf $(OUTDIR)

word-count: $(THESIS).tex
	texcount -merge $<

show: $(PDF)
	@( $(PDFVIEWER) $(PDF) 2> /dev/null; )

bibsort: $(REFERENCES)
	bibtool -s -i $< -o $<

live: $(THESIS).tex $(SOURCE_FILES) | $(OUTDIR) $(CHAPTERS_DIR) $(LATEXMK_RC)
	$(LATEX_COMPILER) -pvc -r $(LATEXMK_RC) $(LATEX_FLAGS) $<

$(PDF): $(THESIS).tex $(SOURCE_FILES) | $(OUTDIR) $(CHAPTERS_DIR)
	$(LATEX_COMPILER) $(LATEX_FLAGS) $<

$(OUTDIR):
	mkdir -p $@

$(CHAPTERS_DIR):
	mkdir -p $@
