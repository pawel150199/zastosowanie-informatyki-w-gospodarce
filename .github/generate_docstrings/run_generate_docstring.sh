#!/bin/bash

generate_docstring=$1

for file in $(find . -name "generate_docstring.py" -prune -o -name "*.py" -print)
do
    python $generate_docstring $file
done