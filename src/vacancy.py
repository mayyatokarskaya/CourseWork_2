class Vacancy:
    """Класс для представления вакансии"""

    def __init__(self, title: str, url: str, salary_from: int = 0, salary_to: int = 0, description: str = ""):
        """конструктор класса"""
        self.title = title
        self.url = url
        self.salary_from = salary_from if salary_from else 0
        self.salary_to = salary_to if salary_to else 0
        self.description = description if description is not None else "Описание отсутствует"

    def get_salary_range(self):
        """Возвращает диапазон зарплаты"""
        if self.salary_from and self.salary_to:
            return (self.salary_from, self.salary_to)
        elif self.salary_from:
            return (self.salary_from, self.salary_from)
        elif self.salary_to:
            return (self.salary_to, self.salary_to)
        else:
            return (0, 0)

    def __str__(self):
        """Красивый вывод информации о вакансии"""
        salary_info = (
            f"{self.salary_from} - {self.salary_to} руб."
            if self.salary_from or self.salary_to
            else "Зарплата не указана"
        )
        return f"{self.title} ({salary_info})\n{self.url}\n{self.description[:100]}..."

    def __lt__(self, other):
        """Сравнение вакансий по зарплате"""
        self_min, self_max = self.get_salary_range()
        other_min, other_max = other.get_salary_range()
        return self_max < other_max

    def __gt__(self, other):
        """Сравнение вакансий по зарплате"""
        return self.salary_from > other.salary_from

    @classmethod
    def from_dict(cls, vacancy_data):
        """Создает объект Vacancy из словаря (JSON)"""
        title = vacancy_data.get("name", "Без названия")
        url = vacancy_data.get("alternate_url", "#")
        salary = vacancy_data.get("salary", {})

        salary_from = salary.get("from") if salary and salary.get("from") else 0
        salary_to = salary.get("to") if salary and salary.get("to") else 0
        description = vacancy_data.get("snippet", {}).get("requirement", "Описание отсутствует")

        return cls(title, url, salary_from, salary_to, description)
