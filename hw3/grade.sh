#!/usr/bin/env bash

rm hw3.py
ls | grep -v 'nodes.py\|grade.sh\|grader.py\|__pycache__' | tr -d '\n' | xargs -0 -I {} mv {} hw3.py
code hw3.py
python3 grader.py