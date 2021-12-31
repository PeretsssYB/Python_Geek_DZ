import sys

# выводим данные о продажах:

if __name__ == '__main__':
    cut = list(map(int, sys.argv[1:]))
    print(cut)
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        line = f.readlines()
        if len(cut) == 2:
            for el in line[cut[0] - 1: cut[1]]:
                print(el.strip())
        elif len(cut) == 1:
            for el in line[cut[0] - 1:]:
                print(el.strip())
        else:
            for el in line:
                print(el.strip())
    exit()
