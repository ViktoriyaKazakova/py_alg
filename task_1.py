# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

import cProfile

#Цикл
def func_v1(n):
    sum_series = 1
    if n > 1:
        prev = 1
        for _ in range(1, n):
            current = prev * -0.5
            sum_series += current
            prev = current
    return sum_series

#100 loops, best of 3: 0.919 usec per loop - 10
#100 loops, best of 3: 5.77 usec per loop - 100
#100 loops, best of 3: 59.8 usec per loop - 1000
#100 loops, best of 3: 607 usec per loop - 10000

#1    0.000    0.000    0.000    0.000 task_1.py:9(func_v1) - 10
#1    0.001    0.001    0.001    0.001 task_1.py:9(func_v1) - 10000
#1    0.006    0.006    0.006    0.006 task_1.py:9(func_v1) - 100000


#Рекурсия
def func_v2(n):
    if n == 1:
        return 1
    return (-0.5) ** (n-1) + func_v2(n - 1)

#100 loops, best of 3: 2.62 usec per loop - 10
#100 loops, best of 3: 29 usec per loop - 100
#RecursionError: maximum recursion depth exceeded in comparison - 1000

#10/1    0.000    0.000    0.000    0.000 task_1.py:54(func_v2) - 10
#100/1    0.000    0.000    0.000    0.000 task_1.py:54(func_v2) - 100
#RecursionError: maximum recursion depth exceeded in comparison - 1000


def func_v3(n):
    b1 = 1
    q = -0.5
    s = (b1 * (1-q**n)) / (1 - q)
    return s

#100 loops, best of 5: 340 nsec per loop - 10
#100 loops, best of 5: 316 nsec per loop - 100
#100 loops, best of 5: 319 nsec per loop - 1000

#1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3) - 10
#1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3) - 100
#1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3) - 10000

def test_func(func):
    sum_5 = [1, 0.5, 0.75, 0.625, 0.6875]
    for i in range(5):
        if round(func(i+1), 4) == sum_5[i]:
            print(f'TEST {i+1} - OK')
        else:
            print(f'TEST {i+1} - ERROR')
    print()

# Проведя анализ можно сказать, что самым быстрым вариантом стало решение с использованием формулы.
# В данном случае сложность алгоритма не зависит от количества входных данных и является постоянной.
#Вариант с рекурсией не отличается по сложности, от первого, но работает медленнее.



