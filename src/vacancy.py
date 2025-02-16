class Vacancy:
    """Класс для представления вакансии"""

    def __init__(self, title: str, url: str, salary_from: int = 0, salary_to: int = 0, description: str = ""):
        """
        :param title: Название вакансии
        :param url: Ссылка на вакансию
        :param salary_from: Нижняя граница зарплаты
        :param salary_to: Верхняя граница зарплаты
        :param description: Краткое описание вакансии
        """
        self.title = title
        self.url = url
        self.salary_from = salary_from if salary_from else 0  # Если зарплата не указана, ставим 0
        self.salary_to = salary_to if salary_to else 0
        self.description = description

    def __str__(self):
        """Красивый вывод информации о вакансии"""
        salary_info = f"{self.salary_from} - {self.salary_to} руб." if self.salary_from or self.salary_to else "Зарплата не указана"
        return f"{self.title} ({salary_info})\n{self.url}\n{self.description[:100]}..."  # Описание сокращаем

    def __lt__(self, other):
        """Сравнение вакансий по зарплате (для сортировки)"""
        return self.salary_from < other.salary_from

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
