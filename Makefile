# Makefile to simplify test and build.

.PHONY: test clean test-env lint style coverage

all: test

build-python:
	python setup.py sdist bdist_wheel

clean:
	rm -rf coverage_html_report .coverage
	rm -rf rhinopics.egg-info
	rm -rf __pycache__
	rm -rf dist
	rm -rf build
	rm -rf venv-dev
	rm -rf .mypy_cache
	rm -rf .pytest_cache

test: lint style
	python -m pytest

lint:
	ruff check .
	mypy rhinopics

style:
	ruff format
	isort --profile black rhinopics

coverage:
	rm -rf coverage_html_report .coverage
	pytest --cov=rhinopics tests --cov-report=html:coverage_html_report

