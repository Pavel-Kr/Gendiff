import pytest
import os
from gendiff import generate_diff


TEST_FILES_DIR = os.path.join('tests', 'fixtures')


@pytest.fixture
def path_1():
    return os.path.join(TEST_FILES_DIR, 'file1.json')


@pytest.fixture
def path_2():
    return os.path.join(TEST_FILES_DIR, 'file2.json')


@pytest.fixture
def expected_diff():
    path = os.path.join(TEST_FILES_DIR, 'expected.txt')
    with open(path) as file:
        expected = file.read()
    return expected


def test_generate_diff(path_1, path_2, expected_diff):
    diff = generate_diff(path_1, path_2)
    assert diff == expected_diff
