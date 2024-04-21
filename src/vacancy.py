class Vacancy:
    """Класс для работы с вакансиями"""
    name: str
    area_name: str
    alternate_url: str
    requirement: str
    responsibility: str
    salary = 0

    def __init__(self, name, area_name, salary, alternate_url, requirement, responsibility):
        self.name = name
        self.area_name = area_name
        self.alternate_url = alternate_url
        self.requirement = requirement
        self.responsibility = responsibility
        self.salary = salary

    def __gt__(self, other):
        if self.salary != 0:
            if self.salary > other.selary:
                return self
            else:
                return other
        else:
            return "Зарплата одной из вакансий не указана"


