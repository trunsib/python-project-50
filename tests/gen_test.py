import pytest
from gendiff.scripts.generate_diff import generate_diff
from pathlib import Path


test_data = Path(__file__).parent / 'test_data'


@pytest.mark.parametrize(
    "filepath1, filepath2, file_answer, form_name",
    [
        ('filepath1.json', 'filepath2.json', 'answer_stylish.txt', 'stylish'),
        ('filepath1.yml', 'filepath2.yml', 'answer_stylish.txt', 'stylish'),
        ('filepath1.json', 'filepath2.json', 'answer_plain.txt', 'plain'),
        ('filepath1.yml', 'filepath2.yml', 'answer_plain.txt', 'plain'),
        ('filepath1.json', 'filepath2.json', 'answer_json.json', 'json'),
        ('filepath1.yml', 'filepath2.yml', 'answer_json.json', 'json'),
    ]
)
def test_generate_diff(filepath1, filepath2, file_answer, form_name):
    path1 = test_data / filepath1
    path2 = test_data / filepath2

    with open(test_data / file_answer) as f:
        corr_answer = f.read()
    assert generate_diff(str(path1), str(path2), form_name) == corr_answer
