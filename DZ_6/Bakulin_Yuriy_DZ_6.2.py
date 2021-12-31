# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
with open(r'D:\PycharmProjects\PythonGeek\DZ_1\Python_Geek_DZ\DZ_6\nginx_logs.txt', 'r', encoding='UTF-8') as file:
    ip = [line[:line.find(' ')] for line in file]

spam_ip = max(set(ip), key=ip.count)
print(spam_ip, ip.count(spam_ip), sep=' | ')
