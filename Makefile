# Makefile to simplify test and build.

.PHONY: test clean test-env lint style coverage

all: test

clean:
	rm -rf coverage_html_report .coverage
	rm -rf rhinopics.egg-info
	rm -rf venv-dev

test: lint style coverage

lint:
	pytest --pylint --pylint-rcfile=.pylintrc --pylint-error-types=CWEF

style:
	flake8
	mypy rhinopics # tests
	pytest --codestyle --docstyle

# coverage:
# 	rm -rf coverage_html_report .coverage
# 	pytest --cov=rhinopics tests --cov-report=html:coverage_html_report
