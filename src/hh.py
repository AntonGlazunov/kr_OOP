import requests
import json
import os
from src.abstract_class import Parser


class HH(Parser):

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 2, "area_id": 113}
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 1:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
