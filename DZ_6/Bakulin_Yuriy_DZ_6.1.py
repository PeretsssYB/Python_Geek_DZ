# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)

with open(r'D:\PycharmProjects\PythonGeek\DZ_1\Python_Geek_DZ\DZ_6\nginx_logs.txt', 'r', encoding='UTF-8') as file:
    content = []
    for line in file:
        remote_addr = line[:line.find(' ')]
        request_type = line[line.find('"') + 1:line.find(' /')]
        requested_resource = line[line.find(' /') + 2: line.find(' HTTP')]
        t = (remote_addr, request_type, requested_resource)
        content.append(t)
    file.close()
print(content)
