# The name of the main .tex file to build.
THESIS = thesis
# List other .tex needed files
REFERENCES = references.bib
TEX_FILES = $(wildcard *.tex chapters/*.tex)
TEX_STYLES = $(wildcard *.sty *.bst)
FIGURES = $(wildcard figs/* figs/*/*)
SOURCE_FILES = $(REFERENCES) $(TEX_FILES) $(TEX_STYLES) $(FIGURES)
# Folder where output will be placed
OUTDIR = _output
CHAPTERS_DIR = $(OUTDIR)/chapters
# Name of the output file
PDF = $(OUTDIR)/$(THESIS).pdf

LATEX_COMPILER = latexmk
LATEX_FLAGS = -pdf -outdir=$(OUTDIR)
PDFVIEWER = xdg-open

.PHONY: all help clean word-count show bibsort live


all: $(PDF)

help:
	@echo "Commands:"
	@echo ""
	@echo "  all         build a PDF version of the thesis"
	@echo "  show        opens the PDF with your favourite reader"
	@echo "  bibsort     autosort the BibTeX file alphabetically"
	@echo "  word-count  counts the number of words, figures, etc."
	@echo "  clean       clean up build and generated files"
	@echo ""

clean:
	rm -rf $(OUTDIR)

word-count: $(THESIS).tex
	texcount -merge $<

show: all
	@( $(PDFVIEWER) $(PDF) 2> /dev/null; )

bibsort: $(REFERENCES)
	bibtool -s -i $< -o $<

$(PDF): $(THESIS).tex $(SOURCE_FILES) | $(OUTDIR) $(CHAPTERS_DIR)
	$(LATEX_COMPILER) $(LATEX_FLAGS) $<

$(OUTDIR):
	mkdir -p $@

$(CHAPTERS_DIR):
	mkdir -p $@
