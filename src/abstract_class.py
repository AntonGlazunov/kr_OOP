
from abc import ABC


class Parser(ABC):

    def __init__(self, file_worker):
        self.file_worker = file_worker.split("/")

    def load_vacancies(self, keyword):
        pass


class Communication(ABC):
    pass
