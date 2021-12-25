# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_scr = set()
tmp = set()
for i in src:
    if i not in tmp:
        unique_scr.add(i)
    else:
        unique_scr.discard(i)
    tmp.add(i)
unique_scr_sort = [i for i in src if i in unique_scr]
print(unique_scr_sort)
