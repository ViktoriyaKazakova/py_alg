# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
# сложно, то используйте метод сортировки, который не рассматривался на уроках


from random import randint


def get_median(array_for_find):

    for i in range(len(array_for_find)):
        median_candidate = array_for_find[i]
        lower = 0
        higher = 0
        equally = 0
        for element in array_for_find[:i] + array_for_find[i+1:len(array_for_find)]:
            if element < median_candidate:
                lower += 1
            elif element > median_candidate:
                higher += 1
            else:
                equally += 1
        if equally - (abs(higher - lower)) >= 0 and (equally - (abs(higher - lower))) % 2 == 0:
            return median_candidate


M = 5
MIN_ITEM = 0
MAX_ITEM = 10

size = 2 * M + 1

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

print('Исходный массив:\n', array)

median = get_median(array)

print('Медиана исходного массива:\n', median)