import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from src.vacancy import Vacancy  # noqa: E402
from src.vacancy_storage import VacancyStorage  # noqa: E402


@pytest.fixture
def temp_storage(tmp_path):
    """Создает временное хранилище вакансий"""
    temp_file = tmp_path / "vacancies.json"
    return VacancyStorage(file_path=str(temp_file))


@pytest.fixture
def sample_vacancies():
    """Создает тестовые вакансии"""
    return [
        Vacancy("Python Developer", "https://example.com/python", 100000, 150000, "Опыт работы с Python"),
        Vacancy("Data Scientist", "https://example.com/ds", 120000, 180000, "Опыт работы с ML"),
        Vacancy("QA Engineer", "https://example.com/qa", 80000, 120000, "Тестирование ПО"),
    ]


def test_save_and_load_vacancies(temp_storage, sample_vacancies):
    """Тест сохранения и загрузки вакансий"""
    temp_storage.save_vacancies(sample_vacancies)
    loaded_vacancies = temp_storage.load_vacancies()

    assert len(loaded_vacancies) == len(sample_vacancies)
    assert loaded_vacancies[0].title == "Python Developer"
    assert loaded_vacancies[1].salary_from == 120000


def test_add_vacancy(temp_storage, sample_vacancies):
    """Тест добавления вакансии"""
    temp_storage.save_vacancies(sample_vacancies)
    new_vacancy = Vacancy("Frontend Developer", "https://example.com/frontend", 90000, 130000, "Опыт с React")
    temp_storage.add_vacancy(new_vacancy)

    loaded_vacancies = temp_storage.load_vacancies()
    assert len(loaded_vacancies) == 4
    assert loaded_vacancies[-1].title == "Frontend Developer"


def test_delete_vacancy(temp_storage, sample_vacancies):
    """Тест удаления вакансии"""
    temp_storage.save_vacancies(sample_vacancies)
    temp_storage.delete_vacancy("Data Scientist")

    loaded_vacancies = temp_storage.load_vacancies()
    assert len(loaded_vacancies) == 2
    assert not any(vac.title == "Data Scientist" for vac in loaded_vacancies)


def test_filter_vacancies(temp_storage, sample_vacancies):
    """Тест фильтрации вакансий по ключевому слову"""
    temp_storage.save_vacancies(sample_vacancies)
    filtered = temp_storage.filter_vacancies("Python")

    assert len(filtered) == 1
    assert filtered[0].title == "Python Developer"


def test_sort_vacancies_by_salary(temp_storage, sample_vacancies):
    """Тест сортировки вакансий по зарплате"""
    sorted_vacancies = temp_storage.sort_vacancies_by_salary(sample_vacancies, reverse=True)

    assert sorted_vacancies[0].title == "Data Scientist"
    assert sorted_vacancies[-1].title == "QA Engineer"


def test_get_top_n_vacancies(temp_storage, sample_vacancies):
    """Тест получения топ-N вакансий по зарплате"""
    top_vacancies = temp_storage.get_top_n_vacancies(sample_vacancies, 2)

    assert len(top_vacancies) == 2
    assert top_vacancies[0].title == "Data Scientist"
