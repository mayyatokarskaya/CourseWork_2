from src.vacancy import Vacancy


def test_vacancy_creation():
    """Тест создания объекта Vacancy"""
    vacancy = Vacancy("Python Developer", "https://example.com", 50000, 70000, "Опыт работы 2 года")

    assert vacancy.title == "Python Developer"
    assert vacancy.url == "https://example.com"
    assert vacancy.salary_from == 50000
    assert vacancy.salary_to == 70000
    assert vacancy.description == "Опыт работы 2 года"


def test_vacancy_default_values():
    """Тест значений по умолчанию"""
    vacancy = Vacancy("QA Engineer", "https://example.com")

    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0
    assert vacancy.description == "Описание отсутствует"


def test_get_salary_range():
    """Тест метода get_salary_range"""
    v1 = Vacancy("Dev", "url", 30000, 50000)
    v2 = Vacancy("Dev", "url", 40000)
    v3 = Vacancy("Dev", "url", salary_to=60000)
    v4 = Vacancy("Dev", "url")

    assert v1.get_salary_range() == (30000, 50000)
    assert v2.get_salary_range() == (40000, 40000)
    assert v3.get_salary_range() == (60000, 60000)
    assert v4.get_salary_range() == (0, 0)


def test_str_representation():
    """Тест строкового представления вакансии"""
    vacancy = Vacancy("Backend Developer", "https://example.com", 80000, 120000, "Django, PostgreSQL")
    expected_str = "Backend Developer (80000 - 120000 руб.)\nhttps://example.com\nDjango, PostgreSQL..."
    assert str(vacancy) == expected_str


def test_vacancy_comparison():
    """Тест сравнения вакансий по зарплате"""
    v1 = Vacancy("Dev1", "url", 40000, 60000)
    v2 = Vacancy("Dev2", "url", 50000, 70000)
    v3 = Vacancy("Dev3", "url", 30000, 40000)

    assert v1 < v2
    assert v2 > v3
    assert not (v1 > v2)
    assert not (v3 > v1)


def test_from_dict():
    """Тест создания вакансии из словаря"""
    vacancy_data = {
        "name": "Data Scientist",
        "alternate_url": "https://example.com",
        "salary": {"from": 100000, "to": 150000},
        "snippet": {"requirement": "Опыт работы 3 года"},
    }

    vacancy = Vacancy.from_dict(vacancy_data)

    assert vacancy.title == "Data Scientist"
    assert vacancy.url == "https://example.com"
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 150000
    assert vacancy.description == "Опыт работы 3 года"


def test_from_dict_with_missing_values():
    """Тест создания вакансии из словаря с отсутствующими значениями"""
    vacancy_data = {}
    vacancy = Vacancy.from_dict(vacancy_data)

    assert vacancy.title == "Без названия"
    assert vacancy.url == "#"
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0
    assert vacancy.description == "Описание отсутствует"
