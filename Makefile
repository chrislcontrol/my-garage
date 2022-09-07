.DEFAULT_GOAL := default_target

PROJECT_NAME := my_garage
PYTHON_VERSION := 3.10.4
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)
DATABASE_PASS := postgres

.pip:
	pip install pip --upgrade

setup-dev: .pip
	pip uninstall -y typing
	pip install -U setuptools
	pip install -r requirements-dev.txt

setup: .pip
	pip uninstall -y typing
	pip install -U setuptools
	pip install -r requirements.txt

collectstatic:
	echo "Running collectstatic"
	 python manage.py collectstatic --noinput

.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup-dev

.clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

.clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr reports/
	rm -fr .pytest_cache/
	rm -f coverage.xml

clean: .clean-build .clean-pyc .clean-test ## remove all build, test, coverage and Python artifacts

pycodestyle:
	echo "Running pycodestyle"
	pycodestyle

flake8:
	echo "Running flake8"
	flake8

code-convention: pycodestyle flake8

test:
	# "Running unit tests"
	 pytest -v --cov-report=term-missing --cov-report=html --cov-report=xml --cov=nix_proxy --cov-fail-under=80

test-lf:
	# "Running unit tests"
	pytest -v --cov-report=term-missing --cov-report=html --cov-report=xml --cov=nix_proxy --cov-fail-under=0 --lf

# Postgres Local
run-postgres:
	docker start nix-proxy-postgres 2>/dev/null || docker run --name nix-proxy-postgres -p 5432:5432 -e POSTGRES_PASSWORD='$(DATABASE_PASS)' -d postgres:10-alpine

# Run Local Server
runserver: clean collectstatic containers-reset
	python manage.py migrate
	python manage.py runserver

default_target: clean collectstatic code-convention test

docker_clear_containers:
	docker stop $(docker ps -aq); docker rm $(docker ps -aq)

containers-up: run-postgres

containers-down:
	docker stop $$(docker ps -aq)

containers-reset: containers-down containers-up

