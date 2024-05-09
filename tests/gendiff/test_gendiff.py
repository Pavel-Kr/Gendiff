import pytest
import os
from gendiff import generate_diff


TEST_FILES_DIR = os.path.join('tests', 'fixtures')

JSON_1_PATH = 'file1.json'
JSON_2_PATH = 'file2.json'
YAML_1_PATH = 'file1.yaml'
YAML_2_PATH = 'file2.yaml'

EXPECTED_STYLISH_PATH = 'expected_stylish.txt'
EXPECTED_PLAIN_PATH = 'expected_plain.txt'
EXPECTED_JSON_PATH = 'expected.json'


@pytest.fixture(scope='function')
def file_path_1(request):
    return os.path.join(TEST_FILES_DIR, request.param)


@pytest.fixture(scope='function')
def file_path_2(request):
    return os.path.join(TEST_FILES_DIR, request.param)


@pytest.fixture(scope='function')
def expected_diff(request):
    path = os.path.join(TEST_FILES_DIR, request.param)
    with open(path) as file:
        expected = file.read()
    return expected


test_params = [
    (JSON_1_PATH, JSON_2_PATH, 'stylish', EXPECTED_STYLISH_PATH),
    (YAML_1_PATH, YAML_2_PATH, 'stylish', EXPECTED_STYLISH_PATH),
    (JSON_1_PATH, JSON_2_PATH, 'plain', EXPECTED_PLAIN_PATH),
    (YAML_1_PATH, YAML_2_PATH, 'plain', EXPECTED_PLAIN_PATH),
    (JSON_1_PATH, JSON_2_PATH, 'json', EXPECTED_JSON_PATH),
    (YAML_1_PATH, YAML_2_PATH, 'json', EXPECTED_JSON_PATH),
]


@pytest.mark.parametrize('file_path_1,file_path_2,format_name,expected_diff',
                         test_params,
                         indirect=['file_path_1', 'file_path_2', 'expected_diff'])
def test_generate_diff(file_path_1, file_path_2, format_name, expected_diff):
    diff = generate_diff(file_path_1, file_path_2, format_name=format_name)
    assert diff == expected_diff


@pytest.mark.parametrize('file_path_1,file_path_2,expected_diff',
                         [
                             (JSON_1_PATH, JSON_2_PATH, EXPECTED_STYLISH_PATH),
                             (YAML_1_PATH, YAML_2_PATH, EXPECTED_STYLISH_PATH),
                         ], indirect=True)
def test_generate_diff_empty_format(file_path_1, file_path_2, expected_diff):
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == expected_diff
