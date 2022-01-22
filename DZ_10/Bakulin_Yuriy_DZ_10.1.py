# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

from itertools import zip_longest

class Matrix:

    def __init__(self, data):
        self.matrix = data

    def __str__(self):
        """Вывод отображения матрицы в консоли"""
        print(f'-' * (len(self.matrix[0]) * 6 + 1))
        for items in self.matrix:
            for item in items:
                print(f'| {item: ^4d}', end='')
            print('|')
        return f'-' * (len(self.matrix[0]) * 6 + 1)

    def __add__(self, other):
        """Сложение матриц поэлементно"""
        matrix_add = []
        for items_self, items_other in zip_longest(self.matrix, other.matrix, fillvalue=0):
            result = list(map(lambda x: x[0] + x[1], zip_longest(items_self, items_other, fillvalue=0)))
            matrix_add.append(result)
        return Matrix(matrix_add)


# Создаем объекты:
m1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])  # матрица 3*3
m2 = Matrix([[4, 5, 6], [6, 7, 8], [10, 11, 12]])  # матрица 3*3
print(m1)
print(m2)
print(m1 + m2)
