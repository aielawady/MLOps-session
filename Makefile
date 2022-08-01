install:
	python -m pip install -U pip && python -m pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py

test:
	python -m pytest -vv
