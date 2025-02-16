from job_api import HeadHunterAPI
from vacancy import Vacancy
from vacancy_storage import VacancyStorage

if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    vacancy_storage = VacancyStorage()

    search_query = input("Введите поисковый запрос: ")
    vacancies_json = hh_api.get_vacancies(search_query, per_page=12)
    vacancies = [Vacancy.from_dict(vac) for vac in vacancies_json]

    print("\nСохранение вакансий в файл...")
    vacancy_storage.save_vacancies(vacancies)

    print("\nЗагруженные вакансии из файла:")
    loaded_vacancies = vacancy_storage.load_vacancies()
    for vac in loaded_vacancies:
        print(vac)

    # Фильтрация по ключевому слову
    keyword = input("\nВведите слово для фильтрации: ")
    filtered_vacancies = vacancy_storage.filter_vacancies(keyword)
    print("\nОтфильтрованные вакансии:")
    for vac in filtered_vacancies:
        print(vac)

    # Фильтрация по зарплате
    min_salary = int(input("\nВведите минимальную зарплату: "))
    max_salary = int(input("Введите максимальную зарплату: "))
    salary_filtered_vacancies = vacancy_storage.filter_vacancies_by_salary(min_salary, max_salary)
    print("\nОтфильтрованные вакансии по зарплате:")
    for vac in salary_filtered_vacancies:
        print(vac)

    # Топ N вакансий по зарплате
    top_n = int(input("\nВведите количество топ вакансий по зарплате: "))
    top_vacancies = vacancy_storage.get_top_n_vacancies(salary_filtered_vacancies, top_n)
    print(f"\nТоп {top_n} вакансий по зарплате:")
    for vac in top_vacancies:
        print(vac)
