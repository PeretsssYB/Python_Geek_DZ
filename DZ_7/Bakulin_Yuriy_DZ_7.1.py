# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

import os
my_dir = 'my_project'
sub_dirs = ['settings', 'mainapp', 'adminapp', 'authapp']
for d in sub_dirs:
    dir_path = os.path.join(my_dir, d)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
