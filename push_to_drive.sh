#!/bin/bash

"/System/Library/Automator/Combine PDF Pages.action/Contents/Resources/join.py" -o eomt-book.pdf images/front-cover.pdf images/front-cover-back.pdf eomt.pdf images/back-cover-back.pdf images/back-cover.pdf
cp eomt-book.pdf /Users/oscar/Google\ Drive/TFM/.
cp slides/eomt-slides.pdf /Users/oscar/Google\ Drive/TFM/. 
