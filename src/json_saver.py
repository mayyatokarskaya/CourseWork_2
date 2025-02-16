import json
import os
from vacancy import Vacancy


class JSONSaver:
    """Класс для работы с JSON-файлом вакансий"""

    FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "vacancies.json")

    def __init__(self, file_path=None):
        """Позволяет задать свой путь к файлу"""
        self.file_path = file_path if file_path else self.FILE_PATH

    def save_vacancies(self, vacancies):
        """Сохраняет список вакансий в JSON-файл"""
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)  # Создаём папку, если её нет
        data = [vac.__dict__ for vac in vacancies]
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_vacancies(self):
        """Загружает вакансии из JSON-файла"""
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Vacancy(**vac) for vac in data]

    def add_vacancy(self, vacancy):
        """Добавляет новую вакансию в JSON-файл"""
        vacancies = self.load_vacancies()  # Загружаем текущие вакансии
        vacancies.append(vacancy)  # Добавляем новую
        self.save_vacancies(vacancies)  # Пересохраняем с обновленным списком

    def delete_vacancy(self, vacancy_title):
        """Удаляет вакансию по названию"""
        vacancies = self.load_vacancies()
        vacancies = [vac for vac in vacancies if vac.title != vacancy_title]
        self.save_vacancies(vacancies)

    def filter_vacancies(self, keyword):
        """Фильтрует вакансии по ключевому слову"""
        vacancies = self.load_vacancies()
        return [vac for vac in vacancies if keyword.lower() in vac.description.lower()]

