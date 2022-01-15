# 93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
# Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
# Были ли особенные строки? Можно ли для них уточнить регулярное выражение?

import re


def log_parse(scr):
    """Функция возвращает кортеж значений из файла по указанному шаблону"""

    reg_phrase = [r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
                  r'\[(.*?)\]', r'\"([A-Z]{3,5})',
                  r'\/\w+\/\w+\_\d+',
                  r'\s[0-9]{3}\s',
                  r'\s[0-9]{3}\s(\d+)']
    return tuple(re.findall(x, scr)[0] for x in reg_phrase)

with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    # line = f.readline()
    # while line:
    #     print(log_parse(line))
    #     line = f.readline()

    count, line = 2500, f.readline()
    while line and count:
        print(log_parse(line))
        count -= 1
        line = f.readline()
