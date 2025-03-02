import json
import os

from src.vacancy import Vacancy


class JSONSaver:
    """Класс для работы с JSON-файлом вакансий"""

    FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "vacancies.json")

    def __init__(self, file_path=None):
        """Позволяет задать свой путь к файлу"""
        self.file_path = file_path if file_path else self.FILE_PATH
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)  # Создаём папку, если её нет

    # def save_vacancies(self, vacancies):
    #     """Сохраняет список вакансий в JSON-файл"""
    #     data = [vac.__dict__ for vac in vacancies]
    #     with open(self.file_path, "w", encoding="utf-8") as file:
    #         json.dump(data, file, ensure_ascii=False, indent=4)

    def save_vacancies(self, vacancies):
        """Сохраняет список вакансий в JSON-файл"""
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        data = [
            {
                "title": vac.title,
                "url": vac.url,
                "salary_from": vac.salary_from,
                "salary_to": vac.salary_to,
                "description": vac.description,
            }
            for vac in vacancies
        ]
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_vacancies(self):
        """Загружает вакансии из JSON-файла"""
        if not os.path.exists(self.file_path) or os.stat(self.file_path).st_size == 0:
            return []

        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Vacancy(**vac) for vac in data]

    def add_vacancy(self, vacancy):
        """Добавляет новую вакансию в JSON-файл"""
        vacancies = self.load_vacancies()
        vacancies.append(vacancy)
        self.save_vacancies(vacancies)

    def delete_vacancy(self, vacancy_title):
        """Удаляет вакансию по названию"""
        vacancies = self.load_vacancies()
        vacancies = [vac for vac in vacancies if vac.title != vacancy_title]
        self.save_vacancies(vacancies)

    def filter_vacancies(self, keyword):
        """Фильтрует вакансии по ключевому слову (без учёта регистра)"""
        vacancies = self.load_vacancies()
        return [vac for vac in vacancies if keyword.lower() in vac.description.lower()]
