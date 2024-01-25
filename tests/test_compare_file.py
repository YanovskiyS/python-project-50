import pytest
import json
from gendiff.compartion import compare_file
from tests import FIXTURES_PATH


@pytest.mark.parametrize("file1, file2, expected_path", [
    (
        f"{FIXTURES_PATH}/file1.json",
        f"{FIXTURES_PATH}/file2.json",
        f"{FIXTURES_PATH}/extended_value_for_example.txt",
    ),
])
def test_diff(file1, file2, expected_path):
    with open(expected_path, "r") as result, \
         open(file1, "r") as cont1, open(file2, "r") as cont2:
        diff_result = json.load(result)
        assert compare_file(json.load(cont1), json.load(cont2)) == diff_result
