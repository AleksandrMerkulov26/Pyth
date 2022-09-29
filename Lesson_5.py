#1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.\
# filename = input('Введите имя файла с расширением: ')
# out_f = open(filename, 'w',encoding='utf-8')
# print('Введите построчно информацию, которая будет записана в файл. Пустой Enter - завершение работы:''\n')
# while True:
#     stroka = input()
#     if stroka == '':
#         break
#     out_f.write(stroka + '\n')
# # out_f.close()
# print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

#2.Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
# my_f = open('3.txt')
# stroka = 0
# total_word = 0
# for i in my_f:
#     stroka += 1
#     marker = 0
#     word = 0
#     for j in i:
#         if j != ' ' and marker == 0:
#             word += 1
#             marker = 1
#         elif j == ' ':
#             marker = 0
#
#     print('В строке ', stroka, ' содержится ', word, 'слов')
#     total_word += word
#
# print('В файле ', my_f.name, 'содержится ', stroka, 'строк и', total_word, ' слов')
# my_f.close()
#print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')



# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

# with open('111.txt', 'r', encoding='utf-8') as f:
#     workers = {}
#     sredn_zp = 0
#     num = 0
#     print('У следующих сотрудников зарплата меньше 20 тыс.руб.:')
#     for line in f:
#         num += 1
#         key, value = line.split()
#         sredn_zp += float(value)
#         if float(value) < 20000:
#             print(f'{key}')
#     print('Средняя величина дохода сотрудников составляет: %.2f' % (sredn_zp / num))
# print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# my_f = open('2.txt')
# for i, num_str in enumerate(my_f):
#     with open("2_out.txt", "a",encoding='utf-8') as file:
#         if (i) == 0:
#             new_line = num_str.replace('One', 'один')
#             file.write(new_line)
#         elif (i) == 1:
#             new_line = num_str.replace('Two', 'два')
#             file.write(new_line)
#         elif (i) == 2:
#             new_line = num_str.replace('Three', 'три')
#             file.write(new_line)
#         elif (i) == 3:
#             new_line = num_str.replace('Four', 'четыре')
#             file.write(new_line)
# #        print(new_line, end='')
# my_f.close()
#print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
# new_list = [el for el in range(1, 20)]
# sum = 0
# with open("home5.txt", "a",encoding='utf-8') as file:
#     for element in new_list:
#         sum += element
#         file.write(str(element))
#         file.write(' ')
#
# print('Сумма числе в файле равна:', sum)
#print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
