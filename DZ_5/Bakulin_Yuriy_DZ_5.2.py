# * Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield

n = int(input("Введите число, до которого, включительно, нужно создать список нечетных чисел: "))
odd_nums = (nums for nums in range(1, n + 1, 2))
print(next(odd_nums))
print(next(odd_nums))
print(odd_nums)
print(*odd_nums)
