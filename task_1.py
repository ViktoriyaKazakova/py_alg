# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).


import random


def bubble_sort(array_to_sort):
    n = 1
    is_change = True
    while n < len(array_to_sort) and is_change is True:
        is_change = False
        for i in range(len(array_to_sort) - 1):
            if array_to_sort[i] < array_to_sort[i + 1]:
                array_to_sort[i], array_to_sort[i + 1] = array_to_sort[i + 1], array_to_sort[i]
                is_change = True

        n += 1


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Исходный массив:\n', array)

bubble_sort(array)

print('Отсортированный массив:\n', array)