#4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 3

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_freq_num = array[0]
freq = {}

print(f'Изначальный массив:\n{array}\n')

for element in array:
    if freq.get(element):
        freq[element] = freq[element] + 1
    else:
        freq[element] = 1
    if freq[element] > freq[max_freq_num]:
        max_freq_num = element

print(f'Чаще всего в массиве втречается число {max_freq_num}')