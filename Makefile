install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

clean:
	python3 -m pip uninstall hexlet-code