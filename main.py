from src.communication_hh_json import CommunicationVacancyJson
from src.utils import search_vacancies
from src.utils import top_vacancies
from src.vacancy import Vacancy

if __name__ == "__main__":
    vacancy_object_list = []
    print("Введите путь хранения файла с вакансиями через '/'")
    user_path = input()
    print("Введите запрос")
    message = input()
    print("Введите колличество требуемых вакансий")
    user_quantity = input()

    user_vacancy = CommunicationVacancyJson(user_path, search_vacancies(message, user_quantity))

    user_vacancy.write_vacancy()

    for vacancy in user_vacancy.sort_list_vacancy():
        vacancy_object_list.append(Vacancy(**vacancy))

    print("Введите колличество вакансий для сортировки")
    number_vacancies = int(input())

    user_top = top_vacancies(number_vacancies)

    for i in user_top:
        print(str(i))
