from abc import ABC, abstractmethod
import requests


class JobAPI(ABC):
    """Абстрактный класс для работы с API сервисов вакансий"""

    @abstractmethod
    def get_vacancies(self, search_query: str, page: int = 0, per_page: int = 10):
        """
        Получает вакансии с сервиса.
        :param search_query: строка запроса (например, "Python разработчик").
        :param page: номер страницы (по умолчанию 0).
        :param per_page: количество вакансий на странице (по умолчанию 10).
        :return: список вакансий.
        """
        pass


class HeadHunterAPI(JobAPI):
    """Класс для работы с API hh.ru"""

    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query: str, page: int = 0, per_page: int = 10):
        """Получает вакансии с hh.ru"""
        params = {
            "text": search_query,  # Поисковый запрос
            "area": 113,  # Код России в hh.ru
            "page": page,
            "per_page": per_page
        }

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code == 200:
            return response.json()["items"]
        else:
            print(f"Ошибка {response.status_code}: {response.text}")
            return []
