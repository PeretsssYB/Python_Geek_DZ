# список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X)
# создаем список кубов нечетных чисел
cube = []
idx = 0
while idx < 1000:
    if idx % 2:
        cube.append(idx)
    idx += 1
num = 0
while num < len(cube):
    cube[num] **= 3
    num += 1
print(cube)
# Вычисляем сумму чисел из списка, сумма цифр которых делится нацело на 7
cube_s = []
sumnum = 0
for numbers in cube:
    idx_s = numbers
    while numbers > 0:
        num_s = numbers % 10
        sumnum += num_s
        numbers = numbers // 10
    if sumnum % 7 == 0:
        cube_s.append(idx_s)
    sumnum = 0
print(sum(cube_s))
#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел
# из этого списка, сумма цифр которых делится нацело на 7.
add = 17
for numbs in range(len(cube_s)):
    cube_s[numbs] += add
sumnumb = 0
for numbrs in cube_s:
    idx_x = numbrs
    while numbrs > 0:
        num_x = numbrs % 10
        sumnumb += num_x
        numbrs = numbrs // 10
    if sumnumb % 7 == 0:
        cube_s.append(idx_x)
    sumnumb = 0
print(sum(cube_s))
