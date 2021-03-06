# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.

def num_translate():
    """Переводит числительные от 1 до 10 с англ на рус"""
    print('Введите число от 1 до 10 на английском:')
    num = input()
    if num.isdigit():
        print(f'"{num}" будет на русском: "{dictionary1[int(num) - 1]}"')
    elif num not in dictionary:
        print('None')
    else:
        print(f'"{num}" переводится на русский как "{dictionary[num]}"')

dictionary = {'one': 'один', 'two': 'два',
              'three': 'три', 'four': 'четыре',
              'five': 'пять', 'six': 'шесть',
              'seven': 'семь', 'eight': 'восемь',
              'nine': 'девять', 'ten': 'десять'
              }
dictionary1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
num_translate()
