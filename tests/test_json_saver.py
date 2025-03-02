import os

import pytest

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture(scope="function")
def json_saver():
    """Создаёт объект JSONSaver для тестов"""
    test_file = "tests/test_vacancies.json"
    os.makedirs(os.path.dirname(test_file), exist_ok=True)  # Создаём папку, если её нет
    json_saver = JSONSaver(test_file)
    yield json_saver
    if os.path.exists(test_file):
        os.remove(test_file)


def test_save_and_load_vacancies(json_saver):
    """Тестируем сохранение и загрузку вакансий"""
    vac1 = Vacancy(title="Dev", url="https://example.com/dev", description="Junior developer")
    vac2 = Vacancy(title="QA", url="https://example.com/qa", description="Junior QA engineer")

    json_saver.save_vacancies([vac1, vac2])

    loaded_vacancies = json_saver.load_vacancies()

    assert len(loaded_vacancies) == 2
    assert loaded_vacancies[0].title == "Dev"
    assert loaded_vacancies[1].title == "QA"


def test_add_vacancy(json_saver):
    """Тестируем добавление вакансии"""
    vac1 = Vacancy(title="Dev", url="https://example.com/dev", description="Junior developer")
    json_saver.add_vacancy(vac1)

    loaded_vacancies = json_saver.load_vacancies()

    assert len(loaded_vacancies) == 1
    assert loaded_vacancies[0].title == "Dev"


def test_delete_vacancy(json_saver):
    """Тестируем удаление вакансии"""
    vac1 = Vacancy(title="Dev", url="https://example.com/dev", description="Junior developer")
    vac2 = Vacancy(title="QA", url="https://example.com/qa", description="Junior QA engineer")
    json_saver.save_vacancies([vac1, vac2])

    json_saver.delete_vacancy("Dev")
    loaded_vacancies = json_saver.load_vacancies()

    assert len(loaded_vacancies) == 1
    assert loaded_vacancies[0].title == "QA"


def test_filter_vacancies(json_saver):
    """Тестируем фильтрацию вакансий по ключевому слову"""
    vac1 = Vacancy(title="Dev", url="https://example.com/dev", description="Junior developer")
    vac2 = Vacancy(title="QA", url="https://example.com/qa", description="Junior QA engineer")
    json_saver.save_vacancies([vac1, vac2])

    filtered_vacancies = json_saver.filter_vacancies("developer")

    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0].title == "Dev"
