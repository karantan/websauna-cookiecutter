# convenience makefile to run buildout and tests

.DEFAULT_GOAL := build


build:
	virtualenv -p python3 venv
	@venv/bin/pip install -r requirements-dev.txt

clean:
	@rm -rf venv

unit:
	@venv/bin/pytest tests

integration:
	@venv/bin/ws-create --no-input 1
	@venv/bin/pip install -e "my_project[test]"
	@cd my_project && ../venv/bin/pytest my_project
	@rm -rf my_project

tests: unit integration