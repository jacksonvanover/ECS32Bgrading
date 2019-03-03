rm hw4.py
ls | grep -v 'run.sh\|hashTableIncomplete.py\|hashTableCorrect.py\|grader.py\|__pycache__' | tr -d '\n' | xargs -0 -I {} mv {} hw4.py
sleep 1
python3 grader.py
code hw4.py