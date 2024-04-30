install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

run-gendiff:
	poetry run gendiff test_files/file1.json test_files/file2.json

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff/lib

coverage-report:
	poetry run pytest --cov=gendiff/lib --cov-report xml

clean:
	python3 -m pip uninstall hexlet-code