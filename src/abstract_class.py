from abc import ABC


class Parser(ABC):

    def load_vacancies(self, keyword):
        pass


class Communication(ABC):

    def __init__(self, file_vacancy, list_vacancy):
        self.file_vacancy = file_vacancy.split("/")
        self.list_vacancy = list_vacancy

    def write_vacancy(self):
        pass

    def read_file_worker(self):
        pass

    def sort_list_vacancy(self):
        pass

    def del_vacancy(self, id_):
        pass
