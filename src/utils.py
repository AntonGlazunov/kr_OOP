from src.hh import HH
from src.vacancy import Vacancy


def search_vacancies():
    """
    Функция для поиска вакансий по запросу
    """
    print("Введите запрос")
    message = input()
    json_vacancies = HH()
    json_vacancies.load_vacancies(message)
    return json_vacancies.vacancies


def top_vacancies():
    """
    Функция для возвращает топ N вакансий
    """
    print("Введите колличество вакансий")
    number_vacancies = int(input())
    Vacancy.sort_vacancy_salary_min()
    return Vacancy.list_object_vacancy[:number_vacancies]
