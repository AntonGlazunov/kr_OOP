from src.hh import HH
from src.vacancy import Vacancy

a = HH("date/file_worker")
a.load_vacancies("Python")
a.write_vacancies()
sss = []
for i in a.sort_list_vacancy():
    sss.append(Vacancy(**i))

a.del_vacancy("97924689")




