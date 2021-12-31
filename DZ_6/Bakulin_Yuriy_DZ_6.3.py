# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий
# из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые
# данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных
# в файлах во много раз меньше объема ОЗУ.

from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as f_name, \
    open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
        names = f_name.read().splitlines()
        hobbies = f_hobby.read().splitlines()
# print(names, hobbies, sep='\n')
if len(names) < len(hobbies):
    raise('Code 1')
else:
    hobby_name = dict(zip_longest(names, hobbies))
    with open('hobby_name_6_3.json', 'w', encoding='utf-8') as f_h_n:
        json.dump(hobby_name, f_h_n, ensure_ascii=False)
    print(hobby_name)
