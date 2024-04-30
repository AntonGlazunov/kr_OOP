import pytest

from src.utils import top_vacancies
from src.vacancy import Vacancy


@pytest.fixture
def add_object_vacancy():
    test_vacancy = [Vacancy("Имя", "открыта", "https://hh.ru/vacancy/92430462",
                            "test", "test2", {"from": 2000, "to": 3000}),
                    Vacancy("Имя1", "открыта1", "https://hh.ru/vacancy/92430462",
                            "test", "test2", {"from": None, "to": 3000}),
                    Vacancy("Имя2", "открыта2", "https://hh.ru/vacancy/92430462",
                            "test", "test2", {"from": 2000, "to": None}),
                    Vacancy("Имя3", "открыта3", "https://hh.ru/vacancy/92430462",
                            "test", "test2", None), ]
    return test_vacancy


def test_init_utils(add_object_vacancy):
    assert top_vacancies(1)[0].name == 'Имя'
