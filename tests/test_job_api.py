import pytest

from src.job_api import HeadHunterAPI


@pytest.fixture
def hh_api():
    return HeadHunterAPI()


def test_get_vacancies_success(mocker, hh_api):
    """Тест успешного получения вакансий"""
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [{"id": "1", "name": "Тестировщик"}]}

    mocker.patch("requests.get", return_value=mock_response)

    vacancies = hh_api.get_vacancies("тестировщик")
    assert isinstance(vacancies, list)
    assert len(vacancies) == 1
    assert vacancies[0]["name"] == "Тестировщик"


def test_get_vacancies_failure(mocker, hh_api):
    """Тест ошибки при запросе вакансий"""
    mock_response = mocker.Mock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"

    mocker.patch("requests.get", return_value=mock_response)

    vacancies = hh_api.get_vacancies("тестировщик")
    assert vacancies == []
