import pytest

from src.hh import HH


@pytest.fixture
def add_object_hh():
    test_hh = HH(1)
    test_hh.load_vacancies("Python")
    return test_hh


def test_init_hh(add_object_hh):
    assert type(add_object_hh.vacancies) == list
