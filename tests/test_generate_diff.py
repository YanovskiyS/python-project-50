from gendiff.generate_diff import generate_diff
from tests import FIXTURES_PATH
import pytest


@pytest.mark.parametrize("file1, file2, expected_path, format", [
    (
        f"{FIXTURES_PATH}/nested_file1.json",
        f"{FIXTURES_PATH}/nested_file2.json",
        f"{FIXTURES_PATH}/expected_value_for_stylish.txt",
        "stylish"
    ),

    (
        f"{FIXTURES_PATH}/nested_file1.yml",
        f"{FIXTURES_PATH}/nested_file2.yml",
        f"{FIXTURES_PATH}/expected_value_for_stylish.txt",
        "stylish"
    ),

    (
        f"{FIXTURES_PATH}/nested_file1.json",
        f"{FIXTURES_PATH}/nested_file2.json",
        f"{FIXTURES_PATH}/expected_value_for_plain.txt",
        "plain"
    ),

    (
        f"{FIXTURES_PATH}/nested_file1.yml",
        f"{FIXTURES_PATH}/nested_file2.yml",
        f"{FIXTURES_PATH}/expected_value_for_plain.txt",
        "plain"
    ),


    (
        f"{FIXTURES_PATH}/nested_file1.json",
        f"{FIXTURES_PATH}/nested_file2.json",
        f"{FIXTURES_PATH}/expected_value_for_json.txt",
        "json"
    ),

    (
        f"{FIXTURES_PATH}/nested_file1.yml",
        f"{FIXTURES_PATH}/nested_file2.yml",
        f"{FIXTURES_PATH}/expected_value_for_json.txt",
        "json"
    )


])
def test_generate_diff(file1, file2, expected_path, format):
    with open(expected_path, 'r') as result:
        assert result.read().strip() == generate_diff(file1, file2, format)
