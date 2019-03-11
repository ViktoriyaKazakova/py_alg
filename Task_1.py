# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

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



# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('Введите трехзначное число: '))

num1 = number % 10
num2 = number % 100 // 10
num3 = number // 100

sum_ = num1 + num2 + num3
prod = num1 * num2 * num3

print(f'Сумма цифр = {sum_}')
print(f'Произведение цифр = {prod}')


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
# Количество используемой памяти зависит от количества разных цифр введеных пользователем, например при вводе 100:
# Памяти использовано под переменные: 80 байт
# А при вводе 225:
# Памяти использовано под переменные: 140 байт
# при вводе 528
# Памяти использовано под переменные: 168 байт