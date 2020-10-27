# 2) Создать словарь Страна:Столица. Создать список стран. Не все
# страны со списка должны сходиться с названиями стран со словаря. С
# помощою оператора in проверить на вхождение элемента страны в
# словарь, и если такой ключ действительно существует вывести
# столицу.

dt_country = {'Ukraine': 'Kyev',
              'France': 'Paris',
              'UK': 'London',
              'Poland': 'Warsawa'
              }
lt_country = ['German', 'Ukraine', 'USA', 'UK', 'German']


for i in lt_country:
    if i in dt_country:
        print(f'Capital of {i} : {dt_country.get(i)}')
