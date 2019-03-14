# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


import random


def merge_sort(array_to_sort):
    if len(array_to_sort) < 2:
        return array_to_sort
    else:
        middle = len(array_to_sort) // 2
        left_part = merge_sort(array_to_sort[:middle])
        right_part = merge_sort(array_to_sort[middle:len(array_to_sort)])
        return merge_parts(left_part, right_part)


def merge_parts(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50

array = [round(random.uniform(MIN_ITEM, MAX_ITEM), 2) for _ in range(SIZE)]

print('Исходный массив:\n', array)

array = merge_sort(array)

print('Отсортированный массив:\n', array)