from job_api import HeadHunterAPI

if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    vacancies = hh_api.get_vacancies(search_query, per_page=5)

    print("\nНайденные вакансии:")
    for vacancy in vacancies:
        print(vacancy["name"], "-", vacancy["alternate_url"])
