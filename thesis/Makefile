# The name of the main .tex file to build.
THESIS = thesis
# List other .tex needed files
TEX_FILES = apalike-doi.bst license.tex references.bib titlepage.tex variables.tex introduccion.tex fundamentos.tex tesseroids-variable-density.tex gradient-boosted-eql.tex fatiando.tex
# Folder where output will be placed
OUTDIR = _output
# Name of the output file
PDF = $(OUTDIR)/$(THESIS).pdf

LATEX_COMPILER = latexmk
LATEX_FLAGS = -pdf -outdir=$(OUTDIR)
PDFVIEWER = xdg-open


all: $(PDF)

clean:
	rm -rf $(OUTDIR)

word-count:
	texcount -merge $(THESIS).tex

show: all
	@( $(PDFVIEWER) $(PDF) 2> /dev/null; )

$(PDF): $(THESIS).tex $(TEX_FILES)
	$(LATEX_COMPILER) $(LATEX_FLAGS) $<
