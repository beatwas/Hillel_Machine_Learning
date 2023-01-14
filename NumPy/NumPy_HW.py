"""
Завдання:

1. Знайти в датасеті таргет та видалити цю колонку з датасету (видаляти за індексом)
2. Перетворити колонки, що залишились в 2D масив (або впевнитись, що це уже 2D масив)
3. Порахувати mean, median, standard deviation для 1-ї колонки
4. Вставити 20 значень np.nan на випадкові позиції в масиві (при використанні звичайного рандому можуть накластись
    позиції, тому знайти рішення, яке гарантує 20 унікальних позицій)
5. Знайти позиції вставлених значень np.nan в 1-й колонці
6. Відфільтрувати массив за умовою: значення в 3-й колонці > 1.5 та значения в 1-й колонці < 5.0
7. Замінити всі значення np.nan на 0
8. Порахувати всі унікальні значення в массиві та вивести їх разом із кількісю
9. Розбити масив по горизонталі на 2 рівні частини (не використовувати абсолютні числа, мають бути два массиви по
    4 колонки)
10.Відсортувати обидва массиви по 1-й колонці: 1-й за збільшенням, 2-й за зменшенням
11.Зібрати обидва массиви в одне ціле
12.Знайти найбільш часто повторюване значення в массиві
13.Написати функцію, яка б множила всі значення в колонці, які менше середнього значения в цій колонці, на 2, і ділила
    інші значення на 4.
14.Застосувати отриману функцію до 3-ї колонки
"""
from random import randint
from statistics import mode

import numpy as np


#   1. Знайти в датасеті таргет та видалити цю колонку з датасету (видаляти за індексом)
my_arr = np.loadtxt('iris.data', delimiter=',', usecols=(0, 1, 2, 3))


#   3. Порахувати mean, median, standard deviation для 1-ї колонки
print(f'Mean: {np.round(np.mean(my_arr[:, 0]), 2)}\n'
      f'Median: {np.round(np.median(my_arr[:, 0]), 2)}\n'
      f'Standard deviation: {np.round(np.std(my_arr[:, 0]), 2)}')

#   4. Вставити 20 значень np.nan на випадкові позиції в масиві (при використанні звичайного рандому можуть накластись
#     позиції, тому знайти рішення, яке гарантує 20 унікальних позицій)
nan_dct = dict()


def is_new(tp):
    if tp not in nan_dct:
        nan_dct[tp] = 1
        my_arr[tp] = np.nan
    else:
        is_new((randint(0, len(my_arr) - 1), randint(0, len(my_arr[1]) - 1)))


for _ in range(20):
    is_new((randint(0, len(my_arr) - 1), randint(0, len(my_arr[1]) - 1)))


#   5. Знайти позиції вставлених значень np.nan в 1-й колонці
nan_in_fcol = list()

for key in nan_dct.keys():
    if key[1] == 0:
        nan_in_fcol.append(key[0] + 1)
nan_in_fcol.sort()

print(f'Rows with np.nan on first place: {nan_in_fcol}')


#   6. Відфільтрувати массив за умовою: значення в 3-й колонці > 1.5 та значения в 1-й колонці < 5.0
arr6 = my_arr[(my_arr[:, 2] > 1.5) & (my_arr[:, 0] < 5.0)]

print('Filtered array by the condition: values in the 3rd column > 1.5 and values in the 1st column < 5.0:')
print(arr6)


#   7. Замінити всі значення np.nan на 0
for i in nan_dct.keys():
    my_arr[i] = 0


#   8. Порахувати всі унікальні значення в массиві та вивести їх разом із кількісю
uniq = np.unique(my_arr, return_counts=True)

print('Unique values in array:')
for i in range(len(uniq[0])):
    print('\t', uniq[0][i], ' - ', uniq[1][i])


#   9. Розбити масив по горизонталі на 2 рівні частини (не використовувати абсолютні числа, мають бути два массиви по
#     4 колонки)
split_arr = np.array_split(my_arr, 2)


def split_show(arr):
    for i in range(len(arr[0])):
        print('\t', arr[0][i], '\t\t', arr[1][i])


#   10.Відсортувати обидва массиви по 1-й колонці: 1-й за збільшенням, 2-й за зменшенням
split_arr[0] = split_arr[0][split_arr[0][:, 0].argsort()]
split_arr[1] = split_arr[1][split_arr[1][:, 0].argsort()[::-1]]

print('Sorted arrays by 1st column: 1st for increase, 2nd for change')
split_show(split_arr)


#   11.Зібрати обидва массиви в одне ціле
new_arr = np.vstack(split_arr)


#   12.Знайти найбільш часто повторюване значення в массиві
flat_array = my_arr.flatten()
print('Most frequently repeated value in array: ', mode(flat_array))


#   13.Написати функцію, яка б множила всі значення в колонці, які менше середнього значения в цій колонці, на 2,
#     і ділила інші значення на 4.
def func_13(arr, col_numb):
    col_numb -= 1
    arr_mean = np.mean(arr[:, col_numb])

    for i in range(len(arr[:, col_numb])):
        if arr[i, col_numb] < arr_mean:
            arr[i, col_numb] *= 2
        else:
            arr[i, col_numb] /= 4


#   14.Застосувати отриману функцію до 3-ї колонки
func_13(my_arr, 3)
