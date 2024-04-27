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
    assert add_object_communication.read_file_worker()[0] == {'accept_incomplete_resumes': False,
                                                              'accept_temporary': False,
                                                              'address': {'building': '16',
                                                                          'city': 'Санкт-Петербург',
                                                                          'description': None,
                                                                          'id': '6320470',
                                                                          'lat': 59.944576,
                                                                          'lng': 30.294973,
                                                                          'metro': {'lat': 59.942577,
                                                                                    'line_id': '16',
                                                                                    'line_name': 'Невско-Василеостровская',
                                                                                    'lng': 30.278254,
                                                                                    'station_id': '16.228',
                                                                                    'station_name': 'Василеостровская'},
                                                                          'metro_stations': [{'lat': 59.942577,
                                                                                              'line_id': '16',
                                                                                              'line_name': 'Невско-Василеостровская',
                                                                                              'lng': 30.278254,
                                                                                              'station_id': '16.228',
                                                                                              'station_name': 'Василеостровская'},
                                                                                             {'lat': 59.952026,
                                                                                              'line_id': '18',
                                                                                              'line_name': 'Фрунзенско-Приморская',
                                                                                              'lng': 30.291338,
                                                                                              'station_id': '18.249',
                                                                                              'station_name': 'Спортивная'}],
                                                                          'raw': 'Санкт-Петербург, Биржевая линия, 16',
                                                                          'street': 'Биржевая линия'},
                                                              'adv_context': None,
                                                              'adv_response_url': None,
                                                              'alternate_url': 'https://hh.ru/vacancy/93657524',
                                                              'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=93657524',
                                                              'archived': False,
                                                              'area': {'id': '2',
                                                                       'name': 'Санкт-Петербург',
                                                                       'url': 'https://api.hh.ru/areas/2'},
                                                              'branding': {'tariff': None, 'type': 'MAKEUP'},
                                                              'contacts': None,
                                                              'created_at': '2024-04-16T17:11:44+0300',
                                                              'department': None,
                                                              'employer': {'accredited_it_employer': False,
                                                                           'alternate_url': 'https://hh.ru/employer/1795976',
                                                                           'id': '1795976',
                                                                           'logo_urls': {
                                                                               '240': 'https://img.hhcdn.ru/employer-logo/5654817.jpeg',
                                                                               '90': 'https://img.hhcdn.ru/employer-logo/5654816.jpeg',
                                                                               'original': 'https://img.hhcdn.ru/employer-logo-original/1008510.jpg'},
                                                                           'name': 'Университет ИТМО',
                                                                           'trusted': True,
                                                                           'url': 'https://api.hh.ru/employers/1795976',
                                                                           'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1795976'},
                                                              'employment': {'id': 'full', 'name': 'Полная занятость'},
                                                              'experience': {'id': 'between1And3',
                                                                             'name': 'От 1 года до 3 лет'},
                                                              'has_test': False,
                                                              'id': '93657524',
                                                              'insider_interview': None,
                                                              'is_adv_vacancy': False,
                                                              'name': 'Junior Python-разработчик в области AI/ML',
                                                              'premium': False,
                                                              'professional_roles': [
                                                                  {'id': '96', 'name': 'Программист, разработчик'}],
                                                              'published_at': '2024-04-16T17:11:44+0300',
                                                              'relations': [],
                                                              'response_letter_required': False,
                                                              'response_url': None,
                                                              'salary': {'currency': 'RUR', 'from': 100000,
                                                                         'gross': True, 'to': None},
                                                              'schedule': {'id': 'fullDay', 'name': 'Полный день'},
                                                              'show_logo_in_search': True,
                                                              'snippet': {'requirement': 'Уверенное знание языка '
                                                                                         '<highlighttext>Python</highlighttext> и '
                                                                                         'связанного прикладного инструментария (IDE, git и '
                                                                                         'т. д.). Уверенное владение принципами SOLID, ООП, '
                                                                                         'паттернами проектирования...',
                                                                          'responsibility': 'Участие в разработке open-source продуктов и '
                                                                                            'индустриальных решений в области машинного '
                                                                                            'обучения и искусственного интеллекта. Участие '
                                                                                            'в исследовательской деятельности...'},
                                                              'sort_point_distance': None,
                                                              'type': {'id': 'open', 'name': 'Открытая'},
                                                              'url': 'https://api.hh.ru/vacancies/93657524?host=hh.ru',
                                                              'working_days': [],
                                                              'working_time_intervals': [],
                                                              'working_time_modes': []}
    assert add_object_communication.sort_list_vacancy()[0] == {'alternate_url': 'https://hh.ru/vacancy/93657524',
                                                                'name': 'Junior Python-разработчик в области AI/ML',
                                                                'requirement': 'Уверенное знание языка <highlighttext>Python</highlighttext> '
                                                                               'и связанного прикладного инструментария (IDE, git и т. д.). '
                                                                               'Уверенное владение принципами SOLID, ООП, паттернами '
                                                                               'проектирования...',
                                                                'responsibility': 'Участие в разработке open-source продуктов и '
                                                                                  'индустриальных решений в области машинного обучения и '
                                                                                  'искусственного интеллекта. Участие в исследовательской '
                                                                                  'деятельности...',
                                                                'salary': {'currency': 'RUR', 'from': 100000,
                                                                           'gross': True, 'to': None},
                                                                'type_': 'Открытая'}
