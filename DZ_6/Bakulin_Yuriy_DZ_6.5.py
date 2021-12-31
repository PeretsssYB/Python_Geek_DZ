# Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к
# обоим исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для
# случая, когда все файлы находятся в разных папках.

import sys
from itertools import zip_longest

users, hobbies, result_file = sys.argv[1:]
if __name__ == '__main__':
    with open('users.csv', 'r', encoding='utf-8') as f_name, \
            open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
        names = f_name.read().splitlines()
        hobbies = f_hobby.read().splitlines()

    hobby_name_gen = ((names, hobbies) for names, hobbies in zip_longest(names, hobbies))
    with open(result_file, 'w', encoding='utf-8') as f_h_n:
        for hobby_name in hobby_name_gen:
            f_h_n.write(f'{hobby_name[0]}: {hobby_name[1]}\n')
