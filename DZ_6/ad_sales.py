import sys

# модуль добавляет данные о продажах

if __name__ == '__main__':
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{sys.argv[1]}\n')
    exit()
