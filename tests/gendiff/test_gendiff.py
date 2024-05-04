import pytest
import os
from gendiff import generate_diff


TEST_FILES_DIR = os.path.join('tests', 'fixtures')


@pytest.fixture
def json_path_nested_1():
    return os.path.join(TEST_FILES_DIR, 'file1.json')


@pytest.fixture
def json_path_nested_2():
    return os.path.join(TEST_FILES_DIR, 'file2.json')


@pytest.fixture
def yaml_path_nested_1():
    return os.path.join(TEST_FILES_DIR, 'file1.yaml')


@pytest.fixture
def yaml_path_nested_2():
    return os.path.join(TEST_FILES_DIR, 'file2.yaml')


@pytest.fixture
def expected_diff_stylish():
    path = os.path.join(TEST_FILES_DIR, 'expected_stylish.txt')
    with open(path) as file:
        expected = file.read()
    return expected


@pytest.fixture
def expected_diff_plain():
    path = os.path.join(TEST_FILES_DIR, 'expected_plain.txt')
    with open(path) as file:
        expected = file.read()
    return expected


@pytest.fixture
def expected_diff_json():
    path = os.path.join(TEST_FILES_DIR, 'expected.json')
    with open(path) as file:
        expected = file.read()
    return expected


def test_generate_diff_stylish_json(json_path_nested_1, json_path_nested_2, expected_diff_stylish):
    diff = generate_diff(json_path_nested_1, json_path_nested_2)
    assert diff == expected_diff_stylish


def test_generate_diff_stylish_yaml(yaml_path_nested_1, yaml_path_nested_2, expected_diff_stylish):
    diff = generate_diff(yaml_path_nested_1, yaml_path_nested_2)
    assert diff == expected_diff_stylish


def test_generate_diff_format_plain_json(json_path_nested_1, json_path_nested_2, expected_diff_plain):
    diff = generate_diff(json_path_nested_1, json_path_nested_2, format_name='plain')
    assert diff == expected_diff_plain


def test_generate_diff_format_plain_yaml(yaml_path_nested_1, yaml_path_nested_2, expected_diff_plain):
    diff = generate_diff(yaml_path_nested_1, yaml_path_nested_2, format_name='plain')
    assert diff == expected_diff_plain


def test_generate_diff_format_json_json(json_path_nested_1, json_path_nested_2, expected_diff_json):
    diff = generate_diff(json_path_nested_1, json_path_nested_2, format_name='json')
    assert diff == expected_diff_json


def test_generate_diff_format_json_yaml(yaml_path_nested_1, yaml_path_nested_2, expected_diff_json):
    diff = generate_diff(yaml_path_nested_1, yaml_path_nested_2, format_name='json')
    assert diff == expected_diff_json
