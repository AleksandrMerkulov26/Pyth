# 1.
# class Matrix:
#     def __init__(self, mx_list):
#         self.mx_list = mx_list
#
#     def __str__(self):
#         for stroka in self.mx_list:
#             for elem in stroka:
#                 print(f"{elem:10}", end="")
#             print()
#         return ''
#
#     def __add__(self, other):
#         for elem_1 in range(len(self.mx_list)):
#             for elem_2 in range(len(other.mx_list[elem_1])):
#                 self.mx_list[elem_1][elem_2] = self.mx_list[elem_1][elem_2] + other.mx_list[elem_1][elem_2]
#         return Matrix.__str__(self)
#
#
# print("Первая матрица получилась:")
# m = Matrix([[-10, 10, 20], [-1, 10, 5], [5, 10, -20], [10, 10, 0]])
# print(m.__str__())
# print("Вторая матрица получилась:")
# new_m = Matrix([[-20, 10, 0], [10, 0, 20], [0, 20, -10], [20, 20, -70]])
# print(m.__str__())
# print("Сумма матриц:")
# print(m.__add__(new_m))

# 2.
# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#     def __init__(self, param):
#         self.param = param
#
#     @property
#     def rashod(self):
#         pass
#
#     @abstractmethod
#     def abstract(self):
#         pass
#
#
# class Palto(Clothes):
#     @property
#     def rashod(self):
#         return f'{self.param / 6.5 + 0.5 :.2f}'
#     #        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'
#
#     def abstract(self):
#         return 'Возвращает решение абстрактной функции для Пальто'
#
#
# class Kostum(Clothes):
#     @property
#     def rashod(self):
#         return f'{2 * self.param + 0.3 :.2f}'
#     #        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'
#
#     def abstract(self):
#         return 'Возвращает решение абстрактной функции для Костюма'
#
#
# my_palto = Palto(400)
# my_kostum = Kostum(55)
#
# print(f'Для пошива пальто нужно: {my_palto.rashod} ткани')
# print(f'Для пошива костюма нужно: {my_kostum.rashod} ткани')
# print(f'Общий расход ткани для пошива пальто и костюма нужно: {str(float(my_palto.rashod) + float(my_kostum.rashod))} ткани')
# print(my_palto.abstract())
# print(my_kostum.abstract())

# 3.
# class Kletka:
#     def __init__(self, count_cell):
#         self.count_cell = int(count_cell)
#
#     def __add__(self, other):
#         return f'В результате объединения двух клеток - размер общей клетки равен: {self.count_cell + other.count_cell} ячеек'
#
#     def __sub__(self, other):
#         rezult = self.count_cell - other.count_cell
#         return f'В результате вычитания двух клеток - размер конечной клетки равен: {rezult} ячеек' if rezult > 0 else 'Операцию вычитания с данными клетками выполнять нельзя, т.к. у второй клетки ячеек больше'
#
#     def __mul__(self, other):
#         return f'В результате умножения двух клеток - создалась общая клетка, количество ячеек в которой равно: {self.count_cell * other.count_cell}'
#
#     def __truediv__(self, other):
#         return f'В результате деления двух клеток - размер конечной клетки равен: {self.count_cell // other.count_cell} ячеек'
#
#     def make_order(self, row):
#         result = ''
#         for i in range(int(self.count_cell / row)):
#             result += '*' * row + '\n'
#         result += '*' * (self.count_cell % row) + '\n'
#         return result
#
#
# c_1 = int(input('Введите количество ячеек в Первой клетке: '))
# c_2 = int(input('Введите количество ячеек во Второй клетке: '))
# n = int(input('Введите количество ячеек в ряду для организации каждой Клетки: '))
# cell_1 = Kletka(c_1)
# cell_2 = Kletka(c_2)
# print(cell_1 + cell_2)
# print(cell_1 - cell_2)
# print(cell_1 * cell_2)
# print(cell_1 / cell_2)
#
# print(f'Результат организации ячеек Первой клетки по рядам по {n} ячеек в каждом ряду:\n{cell_1.make_order(n)}')
# print(f'Результат организации ячеек Второй клетки по рядам по {n} ячеек в каждом ряду:\n{cell_2.make_order(n)}')