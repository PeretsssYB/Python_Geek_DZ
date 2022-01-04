# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских
# папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.

import os
import shutil
from collections import defaultdict
from os.path import relpath

root_dir = r'D:\PycharmProjects\PythonGeek\DZ_1\Python_Geek_DZ\DZ_7\my_project'
my_files = defaultdict(list)
for root, dirs, files in os.walk(root_dir):
   for file in files:
       ext = file.rsplit('.', maxsplit=1)[-1].lower()
       rel_path = relpath(os.path.join(root, file), root_dir)
       my_files[ext].append(rel_path)

dir_path = os.path.join(root_dir, 'templates')
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

files_to_copy = my_files['html']
for f in files_to_copy:
    shutil.copy(os.path.join(root_dir, f), dir_path)
