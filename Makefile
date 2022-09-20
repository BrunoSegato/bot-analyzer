install:
	pip install -U wheel
	pip install -U pip
	pip install -U setuptools
	pip install pipenv
	PIPENV_VENV_IN_PROJECT="enabled" pipenv install --dev --ignore-pipfile --clear