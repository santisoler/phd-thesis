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
			chapters/gradient-boosted-eql.tex \
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
