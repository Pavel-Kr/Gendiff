import pytest
import os
from gendiff import generate_diff


TEST_FILES_DIR = os.path.join('tests', 'fixtures')


@pytest.fixture
def json_path_1():
    return os.path.join(TEST_FILES_DIR, 'file1.json')


@pytest.fixture
def json_path_2():
    return os.path.join(TEST_FILES_DIR, 'file2.json')


@pytest.fixture
def yaml_path_1():
    return os.path.join(TEST_FILES_DIR, 'file1.yaml')


@pytest.fixture
def yaml_path_2():
    return os.path.join(TEST_FILES_DIR, 'file2.yaml')


@pytest.fixture
def expected_diff():
    path = os.path.join(TEST_FILES_DIR, 'expected.txt')
    with open(path) as file:
        expected = file.read()
    return expected


def test_generate_diff_json(json_path_1, json_path_2, expected_diff):
    diff = generate_diff(json_path_1, json_path_2)
    assert diff == expected_diff


def test_generate_diff_yaml(yaml_path_1, yaml_path_2, expected_diff):
    diff = generate_diff(yaml_path_1, yaml_path_2)
    assert diff == expected_diff
