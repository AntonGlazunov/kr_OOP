from src.hh import HH
from src.vacancy import Vacancy
from src.communication_vacancy_JSON import CommunicationVacancyJson

a = HH()
a.load_vacancies("Python")
j = a.vacancies
b = CommunicationVacancyJson("date/file_worker", a.vacancies)
b.write_vacancy()
sss = []
for i in b.sort_list_vacancy():
    sss.append(Vacancy(**i))

Vacancy.sort_vacancy_salary()
for n in Vacancy.list_object_vacancy:
    print(n.salary_min)






