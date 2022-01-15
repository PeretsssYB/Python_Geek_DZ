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

root_dir = r'D:\PycharmProjects\PythonGeek\DZ_1\Python_Geek_DZ\DZ_7\My_project\templates'
for root, dirs, files in os.walk('My_project'):
    if root == root_dir:
        break
    for file in files:
        if file.rsplit('.', 1)[-1].lower() == 'html':
            os.makedirs(os.path.join(root_dir, root.split('\\')[-1]), exist_ok=True)
            shutil.copyfile(os.path.join(root, file), os.path.join(root_dir, os.path.join(root.split('\\')[-1], file)))
