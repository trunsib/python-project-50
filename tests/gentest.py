import pytest
from gendiff.generate_diff import generate_diff
from pathlib import Path


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
    with open(Path() / 'tests/fixtures' / file_answer) as f:
        corr_answer = f.read()
    assert generate_diff(filepath1, filepath2, form_name) == corr_answer
    