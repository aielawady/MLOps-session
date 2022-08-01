install:
    python -m pip install -r requirements.txt
lint:
    pylint --disable=R,C .\main.py 
test:
    pytest -vv