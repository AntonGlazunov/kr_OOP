from src.hh import HH
from src.vacancy import Vacancy
from src.communication_vacancy_JSON import CommunicationVacancyJson
from src.utils import search_vacancies
from src.utils import top_vacancies

vacancy_object_list = []
print("Введите путь хранения файла с вакансиями через '/'")
user_path = input()
user_vacancy = CommunicationVacancyJson(user_path, search_vacancies())

user_vacancy.write_vacancy()

for vacancy in user_vacancy.sort_list_vacancy():
    vacancy_object_list.append(Vacancy(**vacancy))

user_top = top_vacancies()

for i in user_top:
    print(str(i))








