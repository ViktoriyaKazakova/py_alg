import sys


def get_sizeof(x, ids, size=0):
    if id(x) not in ids:
        size += sys.getsizeof(x)
        ids.add(id(x))

    if hasattr(x, '__iter__'):
        if not isinstance(x, str):
            if hasattr(x, 'items'):
                for xx in x.items():
                    get_sizeof(xx, ids, size)
            else:
                for xx in x:
                    get_sizeof(xx, ids, size)

    return size

#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 10000

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

index_min = 0
index_max = 0

print(f'Изначальный массив:\n{array}\n')

for index, element in enumerate(array):
    if element > array[index_max]:
        index_max = index
    if element < array[index_min]:
        index_min = index

sum_min_max = 0

if abs(index_min - index_max) > 1:
    if index_min > index_max:
        from_index = index_max + 1
        to_index = index_min - 1
    else:
        from_index = index_min + 1
        to_index = index_max - 1

    for index in range(from_index, to_index + 1):
        sum_min_max = sum_min_max + array[index]

    print(f'Сумма элементов между минимальным элементом {array[index_min]} на позиции {index_min} и '
          f'максимальным элеметном {array[index_max]} на позиции {index_max} равна {sum_min_max}')
else:
    print(f'Между минимальным и максимальным элементами нет чисел, суммировать нечего (сумма равна нулю)')




print('\n', '*' * 50, '\n')
locals_dict = dict(locals())

mem_size = 0
val_ids = set()

for var, val in locals_dict.items():

    if var in ('sys', 'show_sizeof', 'get_sizeof', 'random'):
        continue

    if id(val) not in val_ids:

        if var[:2] != '__' and var[-1:-3:-1] != '__':
            mem_size += get_sizeof(val, val_ids)
        else:
            continue

    else:
        continue

    val_ids.add(id(val))

print(f'Памяти использовано под переменные: {mem_size} байт')

# Версия и разрядность Python:
# Python 3.7.2

# Разрядность Windows:
# PROCESSOR_ARCHITECTURE=AMD64

# Результаты анализа программы:
# Размер потребляемой памяти линейно зависит от размера массива и практически не зависит от диапазона
#
# SIZE = 100
# MIN_ITEM = 0
# MAX_ITEM = 100
# Памяти использовано под переменные: 1048 байт
#
# SIZE = 1000
# MIN_ITEM = 0
# MAX_ITEM = 100
# Памяти использовано под переменные: 9188 байт
#
# SIZE = 10000
# MIN_ITEM = 0
# MAX_ITEM = 100
# Памяти использовано под переменные: 87788 байт
#
# SIZE = 100
# MIN_ITEM = 0
# MAX_ITEM = 1000
# Памяти использовано под переменные: 1104 байт
#
# SIZE = 100
# MIN_ITEM = 0
# MAX_ITEM = 10000
# Памяти использовано под переменные: 1132 байт
