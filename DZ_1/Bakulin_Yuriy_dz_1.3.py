# склонение слова «процент» во фразе «N процентов».
# Вывод этой фразы на экран отдельной строкой для каждого из чисел в интервале от 1 до 100
for percent in range(1, 101, 1):
    if percent % 10 == 1 and percent != 11:
        print(str(percent) + " процент")
    elif percent % 10 == 2 and percent != 12:
        print(str(percent) + " процента")
    elif percent % 10 == 3 and percent != 13:
        print(str(percent) + " процента")
    elif percent % 10 == 4 and percent != 14:
        print(str(percent) + " процента")
    else:
        print(str(percent) + " процентов")
