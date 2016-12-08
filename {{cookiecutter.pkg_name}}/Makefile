# convenience makefile to run buildout and tests

.DEFAULT_GOAL := build


build:
	virtualenv -p python3 venv
	@venv/bin/pip install -r requirements.txt
	@if [ -f develop_requirements.txt ]; then venv/bin/pip install -r develop_requirements.txt; fi;

clean:
	@rm -rf venv

sort:
	@venv/bin/isort -rc -fas -sl {{cookiecutter.pkg_name}}

tests:
	@venv/bin/pytest {{cookiecutter.pkg_name}}
