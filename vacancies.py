import json
import os

vacancies_list = [
    {
        'name': 'Торговый агент',
        'is_active': '0',
    },
    {
        'name': 'Торговый представитель',
        'is_active': '0'
    },
    {
        'name': 'Водитель-экспедитор',
        'is_active': '0'
    },
    {
        'name': 'Комплектовщик',
        'is_active': '0'
    },
    {
        'name': 'Водитель электропогрузочной техники',
        'is_active': '0'
    },
    {
        'name': 'Водитель ричтрака',
        'is_active': '0'
    },
    {
        'name': 'Упаковщик готовой продукции',
        'is_active': '0'
    },
    {
        'name': 'Оператор-наладчик',
        'is_active': '0'
    },
    {
        'name': 'Оператор производственной линии',
        'is_active': '0'
    }
]

cities_list = [
    "Москва",
    "Санкт-Петербург",
    "Нижний-Новгород"
]


class Vacancy:

    def __init__(self):
        self.vacancies = {}
        self.cities_list = cities_list

        if os.path.isfile("backup.json"):
            with open('backup.json') as outfile:
                self.vacancies = json.load(outfile)
        else:
            vac_id = 0
            for i in cities_list:
                for j in vacancies_list:
                    self.vacancies[str(vac_id)] = {
                        'name': j['name'],
                        'is_active': j['is_active'],
                        'city': i
                    }
                    vac_id += 1
