#!/bin/bash

for f in `find ./ -type f \( -iname \*.jpg -o -iname \*.png \)`; do
    filename=$(basename -- "$f")
    filename="${filename%.*}"
    echo "OCRing $f"
    tesseract $f $filename -l chi_sim+eng
done
