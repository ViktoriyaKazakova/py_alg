# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

import cProfile


# Вариант 1 - Решето

def gen_sieve(n):
    sieve = [i for i in range(n + 1)]
    sieve[0], sieve[1] = 0, 0
    return sieve


def fix_digs(sieve):
    n = len(sieve)
    for i in range(2, n):
        if sieve[i] != 0:
            k = i + i
            while k < n:
                sieve[k] = 0
                k += i


def add_digs(sieve, numbers):
    sieve.append(numbers)
    fix_digs(sieve)


def get_dig(n):
    sieve = gen_sieve(n)
    fix_digs(sieve)
    first_index = 2
    k = 0
    numbers = len(sieve)

    while k != n:
        for i in range(first_index, numbers):
            if sieve[i] != 0:
                k += 1
        add_digs(sieve, numbers)
        first_index = numbers
        numbers += 1

    return sieve[first_index - 1]

#100 loops, best of 3: 108 usec per loop - 10
#100 loops, best of 3: 21.1 msec per loop - 100

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)  -  10
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:10(gen_sieve)
#         1    0.000    0.000    0.000    0.000 task_2.py:11(<listcomp>)
#        21    0.000    0.000    0.000    0.000 task_2.py:16(fix_digs)
#        20    0.000    0.000    0.000    0.000 task_2.py:26(add_digs)
#         1    0.000    0.000    0.000    0.000 task_2.py:31(get_dig)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        22    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        20    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# #ncalls  tottime  percall  cumtime  percall filename:lineno(function)  -  100
#         1    0.000    0.000    0.023    0.023 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:10(gen_sieve)
#         1    0.000    0.000    0.000    0.000 task_2.py:11(<listcomp>)
#       443    0.022    0.000    0.022    0.000 task_2.py:16(fix_digs)
#       442    0.000    0.000    0.023    0.000 task_2.py:26(add_digs)
#         1    0.000    0.000    0.023    0.023 task_2.py:31(get_dig)
#         1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
#       444    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       442    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



# Вариант 2 - без решета

def get_dig2(n):
    lim_nums = 0x7fffffff
    list_digs = []
    result_num = 0
    for i in range(2, lim_nums):
        for k in list_digs:
            if i % k == 0:
                break
        else:
            if n > 0:
                list_digs.append(i)
                n -= 1
            else:
                result_num = k
                break
    return result_num

#100 loops, best of 3: 6.46 usec per loop - 10
#100 loops, best of 3: 284 usec per loop - 100

 # ncalls  tottime  percall  cumtime  percall filename:lineno(function)  - 10
 #        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
 #        1    0.000    0.000    0.000    0.000 task_2.py:79(get_dig2)
 #        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
 #       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ncalls  tottime  percall  cumtime  percall filename:lineno(function) - 100
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_2.py:79(get_dig2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Алгоритм работы с решетом сложен и работает медленно с большими числами
# в связи с тем, что чем больше число в поиске, тем глубже
# нужно растягивать решето и его обрабатывать.
#Без решета, удалось собрать алгоритм с обработкой в один проход,
# как результат, вариант 2 значительно быстрее варианта 1.