# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield:

def odd_gen(n):
    for nums in range(1, n + 1, 2):
        yield nums


odd_to_55 = odd_gen(55)
print(next(odd_to_55))
print(next(odd_to_55))
print(odd_to_55)

odd_to_111 = odd_gen(111)
print(*odd_to_111)
