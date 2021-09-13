# The name of the main .tex file to build.
THESIS = thesis
# List other .tex needed files
REFERENCES = references.bib
TEX_FILES = apalike-doi.bst \
			$(REFERENCES) \
		   	variables.tex \
			chapters/license.tex \
			chapters/titlepage.tex \
			chapters/introduccion.tex chapters/fundamentos.tex \
			chapters/tesseroids-variable-density.tex \
			chapters/eql-gradient-boosted.tex \
			chapters/eql-gradient-boosted-results.tex \
			chapters/fatiando.tex
# Folder where output will be placed
OUTDIR = _output
CHAPTERS_DIR = $(OUTDIR)/chapters
# Name of the output file
PDF = $(OUTDIR)/$(THESIS).pdf

LATEX_COMPILER = latexmk
LATEX_FLAGS = -pdf -outdir=$(OUTDIR)
PDFVIEWER = xdg-open


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

$(PDF): $(THESIS).tex $(TEX_FILES) | $(OUTDIR) $(CHAPTERS_DIR)
	$(LATEX_COMPILER) $(LATEX_FLAGS) $<

$(OUTDIR):
	mkdir -p $@

$(CHAPTERS_DIR):
	mkdir -p $@
