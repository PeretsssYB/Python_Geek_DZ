#Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html

import os

conf_project = {}
with open('config.yaml') as f:
    my_project = dict(map(str.split, f.readlines()))

main_dir = my_project.pop('main_dir')
for folder, val in my_project.items():
    os.makedirs(os.path.join(os.curdir, main_dir, folder), exist_ok=True)
    print(f'Создана папка {folder}')
    for files in val.split(','):
        with open(os.path.join(os.curdir, main_dir, folder, files), 'w') as f:
            print(f'Создан файл {files} в папке {folder}')
