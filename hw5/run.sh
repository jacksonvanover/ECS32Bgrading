rm hw5.py
ls | grep -v 'run.sh\|grader.py\|__pycache__' | tr -d '\n' | xargs -0 -I {} mv {} hw4.py
sleep 1
python3 grader.py
code hw5.py