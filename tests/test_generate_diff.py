from gendiff.gendiff import generate_diff


data_for_test = open('tests/fixtures/extended_value_for_example.txt', 'r')
file_path1 = 'tests/fixtures/fiel1.json'
file_path2 = 'tests/fixtures/file2.json'


def test_generate_diff():
    with open('tests/fixtures/extended_value_for_example.txt', 'r') as result:
        assert result.read() == generate_diff(file_path1, file_path2)
