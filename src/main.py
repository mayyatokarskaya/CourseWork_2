from job_api import HeadHunterAPI
from vacancy import Vacancy
from json_saver import JSONSaver

if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    json_saver = JSONSaver()

    search_query = input("Введите поисковый запрос: ")
    vacancies_json = hh_api.get_vacancies(search_query, per_page=5)
    vacancies = [Vacancy.from_dict(vac) for vac in vacancies_json]

    print("\nСохранение вакансий в файл...")
    json_saver.save_vacancies(vacancies)

    print("\nЗагруженные вакансии из файла:")
    loaded_vacancies = json_saver.load_vacancies()
    for vac in loaded_vacancies:
        print(vac)

    keyword = input("\nВведите слово для фильтрации: ")
    filtered_vacancies = json_saver.filter_vacancies(keyword)
    print("\nОтфильтрованные вакансии:")
    for vac in filtered_vacancies:
        print(vac)


