# Makefile for Orchestra Platform

build:
    python setup.py build

clean:
    rm -rf build/
    rm -rf dist/

install:
    python setup.py install

test:
    python -m unittest discover -s tests/