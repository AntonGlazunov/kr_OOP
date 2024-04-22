class Vacancy:
    """Класс для работы с вакансиями"""
    name: str
    area_name: str
    alternate_url: str
    requirement: str
    responsibility: str

    def __init__(self, name, area_name, salary, alternate_url, requirement, responsibility):
        self.name = name
        self.area_name = area_name
        self.alternate_url = alternate_url
        self.requirement = requirement
        self.responsibility = responsibility
        if salary.get("from") in None:
            self.salary = "Зарплата не указана"
        else:
            self.salary = salary.get("from")

    def __gt__(self, other):
        if self.salary and other.selary in "Зарплата не указана":
            return "У предложенных вакансий не указана зарплата"
        elif self.salary in "Зарплата не указана":
            return other
        elif other.salary in "Зарплата не указана":
            return self
        elif self.salary > other.salary:
            return self
        else:
            return other


