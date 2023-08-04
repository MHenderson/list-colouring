all: colour

demo: src/demo.py
	poetry run python $<

colour: src/colour-petersen.py
	poetry run python $<