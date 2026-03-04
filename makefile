# Makefile for Python game

# Python interpreter
PYTHON = python3

# Default target
all: run

# Run the game
run:
	$(PYTHON) main.py

# Clean up cache and temporary files
clean:
	rm -rf __pycache__ */__pycache__ *.pyc 

# Rebuild (clean + run)
rebuild: clean run