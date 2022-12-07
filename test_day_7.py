import pytest


@pytest.fixture()
def data():
    with open("./day_7_data.txt") as data_file:
        data = data_file.readlines()

    return data

def test_dir_tree(data):
    pass



