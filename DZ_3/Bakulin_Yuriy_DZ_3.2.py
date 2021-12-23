# (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы —
# результат тоже должен быть с заглавной.
def num_translate_adv():
    number = input('Введите число на английском: \n')
    if number.istitle():
        print(dictionary.get(number.lower()).title())
    else:
        print(dictionary.get(number))
    return number
dictionary = {'one': 'один', 'two': 'два',
              'three': 'три', 'four': 'четыре',
              'five': 'пять', 'six': 'шесть',
              'seven': 'семь', 'eight': 'восемь',
              'nine': 'девять', 'ten': 'десять'
              }
num_translate_adv()
