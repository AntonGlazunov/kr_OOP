import requests

from src.abstract_class import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 1:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    # def write_vacancies(self):
    #     with open(os.path.join(*self.file_worker), 'w', encoding="utf-8") as file:
    #         file.write(json.dumps(self.vacancies))


# a = HH("../date/file_worker")
# a.load_vacancies("Менеджер по продажам автомобилей")
# a.write_vacancies()
# def read_file():
#     with open(os.path.join("..", "date", "file_worker"), 'r', encoding="utf-8") as file:
#         file_1 = json.loads(file.read())
#         return file_1

# print(read_file())