# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки.')


class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки с помощью {self.title}')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки с помощью {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки с помощью {self.title}')


tool_1 = Pen('Ручка')
tool_1.draw()
tool_2 = Pen('Карандаш')
tool_2.draw()
tool_3 = Pen('Маркер')
tool_3.draw()
Stationery.draw(tool_2)
