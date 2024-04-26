import json
import os

from src.abstract_class import Communication


class CommunicationVacancyJson(Communication):

    def __init__(self, file_vacancy, list_vacancy):
        super().__init__(file_vacancy, list_vacancy)

    def write_vacancy(self):
        with open(os.path.join(*self.file_vacancy), 'w', encoding="utf-8") as file:
            file.write(json.dumps(self.list_vacancy))

    def read_file_worker(self):
        with open(os.path.join(*self.file_vacancy), 'r', encoding="utf-8") as file:
            list_vacancy = json.loads(file.read())
            return list_vacancy

    def sort_list_vacancy(self):
        sort_list_vacancy = []
        for vacancy in self.read_file_worker():
            sort_list_vacancy.append({"name": vacancy["name"], "type_": vacancy["type"]["name"],
                                      "alternate_url": vacancy["alternate_url"],
                                      "requirement": vacancy["snippet"]["requirement"],
                                      "responsibility": vacancy["snippet"]["responsibility"],
                                      "salary": vacancy["salary"]})
        return sort_list_vacancy

    def del_vacancy(self, id_):
        file_worker = self.read_file_worker()
        for vacancy in file_worker:
            if id_ in vacancy.get("id"):
                file_worker.remove(vacancy)
        with open(os.path.join(*self.file_vacancy), 'w', encoding="utf-8") as file:
            file.write(json.dumps(file_worker))
