import pytest

from src.communication_vacancy_json import CommunicationVacancyJson
from src.hh import HH


@pytest.fixture
def add_object_communication():
    hh_test = HH(2)
    hh_test.load_vacancies("Python")
    communication_test = CommunicationVacancyJson("../date/file_test", hh_test.vacancies)
    communication_test.write_vacancy()
    return communication_test


def test_init_communication_vacancy_json(add_object_communication):
    assert type(add_object_communication.read_file_worker()[0]) == dict
    assert type(add_object_communication.sort_list_vacancy()[0]) == dict
