import pytest

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


def test_init_vacancy(add_object_vacancy):
    assert str(add_object_vacancy[0]) == (
        'Вакансия: Имя, ссылка: https://hh.ru/vacancy/92430462, предлагаемая зарплата: от 2000 рублей')
    assert add_object_vacancy[0].name == "Имя"
    assert add_object_vacancy[0].type_ == "открыта"
    assert add_object_vacancy[0].alternate_url == "https://hh.ru/vacancy/92430462"
    assert add_object_vacancy[0].requirement == "test"
    assert add_object_vacancy[0].responsibility == "test2"
    assert add_object_vacancy[0].salary == {"from": 2000, "to": 3000}
    assert add_object_vacancy[3].salary == 0
    assert add_object_vacancy[1].salary_min == 0
    assert add_object_vacancy[1].salary_max == 3000
    assert add_object_vacancy[2].salary_min == 2000
    assert add_object_vacancy[2].salary_max == 0
