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



# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input('Введите любое натуральное число: '))

left_part = 0
right_part = 0

for i in range(n):
    left_part += i + 1

right_part = n * (n + 1) / 2

print(f'1+2+...+n = {left_part}')
print(f'n(n+1)/2 = {right_part}')

if left_part != right_part:
    print(f'Формула не верна: {left_part} <> {right_part}')
else:
    print(f'Формула верна: {left_part} = {right_part}')



print('\n', '*' * 50, '\n')
locals_dict = dict(locals())

mem_size = 0
val_ids = set()

for var, val in locals_dict.items():

    if var in ('sys', 'show_sizeof', 'get_sizeof'):
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
# Потребление памяти медленно растет при увеличении числа n

# Введите любое натуральное число: 1
# Памяти использовано под переменные: 76 байт

# Введите любое натуральное число: 10
# Памяти использовано под переменные: 108 байт

# Введите любое натуральное число: 100
# Памяти использовано под переменные: 108 байт

# Введите любое натуральное число: 1000
# Памяти использовано под переменные: 108 байт

# Введите любое натуральное число: 10000
# Памяти использовано под переменные: 108 байт

# Введите любое натуральное число: 100000
# Памяти использовано под переменные: 112 байт