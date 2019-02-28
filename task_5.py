#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

import random

SIZE = 20
MIN_ITEM = -10
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Изначальный массив:\n{array}\n')

if MIN_ITEM < 0:
    max_negative = MIN_ITEM
    for index, element in enumerate(array):
        if max_negative <= element < 0:
            max_negative = element
            max_negative_index = index
    print(f'Максимальный отрицательный элемент стоит на позиции {max_negative_index} и имеет значение {max_negative}')
else:
    print('В массиве нет отрицательных элементов!')