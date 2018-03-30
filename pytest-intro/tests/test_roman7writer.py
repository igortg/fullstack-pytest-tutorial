import shutil
import pytest
from pathlib import Path
from roman7writer import write_to_roman

@pytest.mark.skip(reason="This test do not clean up. Should not run")
def test_naive_roman_writer():
    text = "In the Book 3 Chapter 7 of the 2 Collection"
    output_file = 'roman.txt'
    write_to_roman(text, output_file)
    with open(output_file) as output:
        assert output.read() == "In the Book III Chapter VII of the II Collection"


@pytest.fixture()
def data_folder():
    data_path = Path('test_roman')
    data_path.mkdir()
    yield data_path
    shutil.rmtree(str(data_path))


def test_roman_writer1(data_folder):
    text = "In the Book 3 Chapter 7 of the 2 Collection"
    output_file = data_folder/'roman.txt'
    write_to_roman(text, str(output_file))
    assert output_file.read_text() == "In the Book III Chapter VII of the II Collection"


def test_roman_writer2(tmp_data_folder):
    text = "In the Book 3 Chapter 7 of the 2 Collection"
    output_file = tmp_data_folder/'roman.txt'
    write_to_roman(text, str(output_file))
    assert output_file.read_text() == "In the Book III Chapter VII of the II Collection"


def test_roman_writer3(tmpdir):
    text = "In the Book 3 Chapter 7 of the 2 Collection"
    output_file = tmpdir.mkdir('test_romans').join('roman.txt')
    write_to_roman(text, str(output_file))
    assert output_file.read() == "In the Book III Chapter VII of the II Collection"



