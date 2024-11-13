.PHONY: project_black
black:
	black this_package test setup.py --check

.PHONY: project_flake
flake:
	flake8 this_package test setup.py

.PHONY: project_test
test:
	pytest

.PHONY: check
check: black flake test interrogate

# Setup -----------------------------------------------------------------------

.PHONY: setup
setup:
	python -m pip install --upgrade pip
	python -m pip install pdm

.PHONY: install_dev
install_dev:
	pdm install -G:all
	echo $(shell pwd)/src > "$(shell python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')/src-library.pth"
	echo $(shell pwd)/ >> "$(shell python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')/src-library.pth"
	

.PHONY: install_prod
install_prod:
	pip install --upgrade pip
	pip install pdm
	pdm install --prod

# Project ---------------------------------------------------------------------

.PHONY: project_clean
clean:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ ./notabooks/ipynb_checkpoints .pytest_cache ./dist ./volumes

.PHONY: project_restore
restore:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ ./notabooks/ipynb_checkpoints .pytest_cache ./dist .venv poetry.lock

.PHONY: project_test_coverage
test_coverage:
	pytest --cov --cov-report term --cov-report html:logs/coverage_log --typeguard-packages=faradai

.PHONY: build_package
build_package:
	poetry build


# Mkdocs ----------------------------------------------------------------------

.PHONY: docs_launch
docs_launch:
	mkdocs serve

.PHONY: docs_build
docs_build:
	mkdocs build

.PHONY: docs_launch_docker
docs_launch_docker:
	mkdocs build
	mkdocs serve --dev-addr=0.0.0.0:8000

.PHONY: docs_debug_docker
docs_launch_debug_docker:
	mkdocs build
	mkdocs serve -v --dev-addr=0.0.0.0:8000

.PHONY: docs_test
docs_test:
	mkdocs build --verbose --site-dir public_tmp  # --strict 

.PHONY: docs_deploy-github
docs_deploy:
	mkdocs build
	mkdocs gh-deploy --force

.PHONY: docs_public
docs_public:
	mkdocs build -c --verbose --site-dir public
