import json
import os

from vacancy import Vacancy


class VacancyStorage:
    """Класс для работы с вакансиями в JSON-файле"""

    FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "vacancies.json")

    def __init__(self, file_path=None):
        """Позволяет задать свой путь к файлу"""
        self.file_path = file_path if file_path else self.FILE_PATH

    def load_vacancies(self):
        """Загружает вакансии из JSON-файла"""
        if not os.path.exists(self.file_path):
            return []  # Если файл не существует, возвращаем пустой список
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Vacancy(**vac) for vac in data]  # Преобразуем в объекты Vacancy

    def save_vacancies(self, vacancies):
        """Сохраняет список вакансий в JSON-файл"""
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        data = [
            {
                "title": vac.title,
                "url": vac.url,
                "salary_from": vac.salary_from,
                "salary_to": vac.salary_to,
                "description": vac.description
            }
            for vac in vacancies
        ]
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

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
        """Фильтрует вакансии по ключевому слову"""
        vacancies = self.load_vacancies()
        return [vac for vac in vacancies if keyword.lower() in vac.description.lower()]

    def filter_vacancies_by_salary(self, min_salary, max_salary):
        """Фильтрует вакансии по диапазону зарплат"""
        vacancies = self.load_vacancies()
        filtered_vacancies = [
            vac for vac in vacancies if vac.salary_from >= min_salary and vac.salary_to <= max_salary
        ]
        return filtered_vacancies

    def sort_vacancies_by_salary(self, vacancies, reverse=False):
        """Сортирует вакансии по зарплате (по убыванию или возрастанию)"""
        return sorted(vacancies, key=lambda vac: (vac.salary_from + vac.salary_to) / 2, reverse=reverse)

    def get_top_n_vacancies(self, vacancies, n):
        """Возвращает топ N вакансий по зарплате"""
        sorted_vacancies = self.sort_vacancies_by_salary(vacancies, reverse=True)
        return sorted_vacancies[:n]
