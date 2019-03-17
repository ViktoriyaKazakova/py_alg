#1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
#состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

def count_substr(input_string):
    hash_set = set()

    window = len(input_string) - 1

    while window > 0:

        for i in range(len(input_string) - window + 1):
            hash_set.add(hash(input_string[i:i + window]))

        window -= 1

    return len(hash_set)


string = input('Введите строку (из диапазона символов [a-z]): ')

uniq_sub_strings = count_substr(string)

print(f'Уникальных подстрок {uniq_sub_strings}')