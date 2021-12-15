f_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for wor, num in enumerate(f_list):
    if num.isdigit():
        f_list[wor] = f'"{int(num):02d}"'
    elif num[1:].isdigit():
        f_list[wor] = f'"{num[0]}{int(num[1:]):02d}"'
    print(f_list[wor], end=' ')
print('\n', '\n', f_list)