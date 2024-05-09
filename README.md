### Hexlet tests and linter status:
[![Actions Status](https://github.com/Pavel-Kr/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Pavel-Kr/python-project-50/actions)
[![Main workflow](https://github.com/Pavel-Kr/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/Pavel-Kr/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/e2db2dbcff365ffdd2ab/maintainability)](https://codeclimate.com/github/Pavel-Kr/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e2db2dbcff365ffdd2ab/test_coverage)](https://codeclimate.com/github/Pavel-Kr/python-project-50/test_coverage)

## Gendiff
Difference generator for configuration files. Supports JSON and YAML input file formats. Output can be shown in stylish, plain or JSON format, use `-f` flag to specify output format.

### Installation
Gendiff requires poetry for installation. Detailed guide on how to install poetry can be found [here](https://python-poetry.org/docs/#installation). After you install poetry, run `make install build package-install`

### Usage
    gendiff [-h] [-f FORMAT] first_file second_file

      first_file - path to the first file
      second_file - path to the second file

    options:
      -h, --help            show help message and exit
      -f FORMAT, --format FORMAT
                            set format for output
Format parameter can accept one of 3 values: `stylish`, `plain` or `json`. If no format specified, then `stylish` is used as the default format.

### Demo
[Gendiff JSON](https://asciinema.org/a/Ldp4ORCzxOpwiQ0TOeDvXcaKu)

[Gendiff YAML](https://asciinema.org/a/nIrGOfY5dhNMI0MOqtTVejiaX)

[Gendiff nested structures](https://asciinema.org/a/jIVsXEkvcNdb0ycVZWVsmYmdA)

[Plain output format](https://asciinema.org/a/gpDv4QLvjGnf5QWmfFCfsm7Us)

[JSON output format](https://asciinema.org/a/39yFEKJVQMbipWeITUFe2HVX3)