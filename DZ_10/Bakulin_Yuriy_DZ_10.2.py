# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Wear(ABC):

    # def __init__(self, cloth):
    #     self.cloth = cloth

    @abstractmethod
    def cloth_cost(self):
        pass


class Coat(Wear):

    def __init__(self, size):
        self.size = size

    @property
    def cloth_cost(self):
        return self.size / 6.5 + 0.5


class Costume(Wear):

    def __init__(self, height):
        self.height = height

    @property
    def cloth_cost(self):
        return 2 * self.height + 0.3


coat = Coat(1500)
costume = Costume(110)
print(f'Расход ткани на 1 костюм: {costume.cloth_cost}\n'
      f'Расход ткани на 1 пальто: {coat.cloth_cost}')
