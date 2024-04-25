from src.hh import HH
from src.vacancy import Vacancy
import json
import os


a = HH("date/file_worker")
a.load_vacancies("Python")

c = a.vacancies
list_vacancy = []
# def read_file():
#     with open(os.path.join("date", "file_worker"), 'r', encoding="utf-8") as file:
#         worker = json.loads(file.read(), cls=VacancyDecoder)
#         return worker

for i in c:
    list_vacancy.append(Vacancy(i["name"], i["type"]["name"],
                                i["alternate_url"], i["snippet"]["requirement"], i["snippet"]["responsibility"],
                                i["salary"]))

print(list_vacancy[1].salary)
print(list_vacancy[0].salary)
print(list_vacancy[2].salary)
bc = list_vacancy[0] > list_vacancy[1]
asd = list_vacancy[2] > list_vacancy[0]
sdfg = list_vacancy[0] > list_vacancy[2]
print(bc)
print(asd)
print(sdfg)

