#!/bin/bash

echo "Compiling eomt!"

pdflatex eomt # Compile template
makeindex eomt.nlo -s nomencl.ist -o eomt.nls # Compile nomenclature
makeindex eomt # Compile index
biber eomt # Compile bibliography
makeglossaries eomt # Compile glossary
pdflatex eomt # Compile template again
pdflatex eomt # Compile template again
