# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
from requests import get, utils
from decimal import Decimal

def currency_rates(val_code):
    """Функция получения данных о текущем курсе валюты"""

    target_url = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(target_url.headers)
    target_content = target_url.content.decode(encoding=encodings)
    exchange_date = target_content[target_content.find('Date=')+6:target_content.find('name')-2]  # Достаем дату курса
    key_words = ['Nominal', 'Name', 'Value']  # Список тегов XML для поиска требуемых параметров
    target_str = target_content[target_content.find(str(val_code).upper()):]  # Поиск валюты в общем списке

    if len(target_str) > 2:
        target_str = target_str[:target_str.find('</Valute>')]  # Формируем строку с целевой информацией о нужной валюте

        # Формирование списка информации о валюте по тегам XML и приведение их к нужному типу

        currency_info = list(map(lambda x: str(target_str.split(x)[1])[1:-2], key_words))
        currency_info[0] = int(currency_info[0])
        # currency_info[2] = float('.'.join(currency_info[2].split(',')))
        currency_info[2] = Decimal(currency_info[2].replace(',', '.')).quantize(Decimal('0.01'))
        print(f'Курс актуален на: {exchange_date} \n{currency_info[0]} {currency_info[1]} сегодня меняют на {currency_info[2]} руб.')
    else:
        print('Курс валюты не найден/Неккоректный код валюты')


print(f'Введите код валюты, курс которой хотите узнать: ')
val_code = input()
currency_rates(val_code)
