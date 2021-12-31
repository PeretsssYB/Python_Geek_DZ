#  Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
#  (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
#  Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей
#  и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
#  Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны
#  храниться данные, полученные в результате парсинга.

from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as f_name, \
    open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
        names = f_name.read().splitlines()
        hobbies = f_hobby.read().splitlines()

hobby_name_gen = ((names, hobbies) for names, hobbies in zip_longest(names, hobbies))
with open('hobby_name_gen_6_4.txt', 'w', encoding='utf-8') as f_h_n:
    for hobby_name in hobby_name_gen:
        f_h_n.write(f'{hobby_name[0]}: {hobby_name[1]}\n')
