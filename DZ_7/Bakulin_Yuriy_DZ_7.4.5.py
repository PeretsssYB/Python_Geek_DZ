# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
# размера файла (пусть будет кратна 10), а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт

import os
import json

root_dir = r'D:\PycharmProjects\PythonGeek\DZ_1\Python_Geek_DZ\DZ_7'
size_files = {}
for root, dirs, files in os.walk(root_dir):
    for file in files:
        s_dict = os.stat(os.path.join(root, file)).st_size // 10 * 10 + 10
        f_ext = file.rsplit('.')[-1]
        if s_dict in size_files:
            size_files[s_dict][1].append(f_ext)
            size_files[s_dict] = (size_files[s_dict][0] + 1, list(set(size_files[s_dict][1])))
        else:
            size_files.setdefault(s_dict, (1, [f_ext]))

result = {k: size_files[k] for k in sorted(size_files.keys())}
print(result)
with open('DZ_7_summary.json', 'w') as f:
    json.dump(result, f)
with open('DZ_7_summary.json', 'r') as f:
    print(json.load(f))
