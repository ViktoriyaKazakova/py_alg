#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

index_min = 0
index_max = 0

print(f'Изначальный массив:\n{array}\n')

for index, element in enumerate(array):
    if element > array[index_max]:
        index_max = index
    if element < array[index_min]:
        index_min = index

array[index_max], array[index_min] = array[index_min], array[index_max]

print(f'Массив в котором первый максимальный и первый минимальный элементы поменяны местами:\n{array}\n')