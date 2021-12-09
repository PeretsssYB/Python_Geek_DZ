# вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах
# 87990 = 1 d 0 ho 26 mi 30 se
s = 1  # seconds
m = 60  # minutes
h = 3600  # hours
d = 86400  # days

duration = input("введите количество секунд: ")

if int(duration) >= d:
    day = int(duration) // d
    hour = int(duration) % d // h
    minute = int(duration) % d % h // m
    sec = int(duration) % d % h % m
    print(str(day) + " дн " + str(hour) + " час " + str(minute) + " мин " + str(sec) + " сек ")
elif int(duration) >= h:
    hour = int(duration) // h
    minute = int(duration) % h // m
    sec = int(duration) % h % m
    print(str(hour) + " час " + str(minute) + " мин " + str(sec) + " сек ")
elif int(duration) >= m:
    minute = int(duration) // m
    sec = int(duration) % m
    print(str(minute) + " мин " + str(sec) + " сек ")
else:
    sec = int(duration)
    print(str(sec) + ' сек ')
