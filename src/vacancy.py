class Vacancy:
    """Класс для работы с вакансиями"""
    name: str
    area_name: str
    alternate_url: str
    requirement: str
    responsibility: str

    def __init__(self, name, type_, alternate_url, requirement, responsibility, salary=None):
        self.name = name
        self.type_ = type_
        self.alternate_url = alternate_url
        self.requirement = requirement
        self.responsibility = responsibility
        if salary is None:
            self.salary = "Зарплата не указана"
        elif salary["from"] is None:
            self.salary = salary.get("to")
        else:
            self.salary = salary.get("from")

    def __gt__(self, other):
        try:
            if self.salary == "Зарплата не указана" and other.salary == "Зарплата не указана":
                raise ValueError
            elif self.salary == "Зарплата не указана":
                return other
            elif other.salary == "Зарплата не указана":
                return self
            elif self.salary > other.salary:
                return self
            else:
                return other
        except ValueError:
            return "У предложенных вакансий не указана зарплата"

    def __str__(self):
        return f"Вакансия: {self.name}, ссылка: {self.alternate_url}, предлагаемая зарплата: {self.salary}"


