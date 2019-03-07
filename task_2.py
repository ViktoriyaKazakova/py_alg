# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


HEX = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


def add_numbers(a, b):
    sum_ = deque()
    a = deque(a)
    b = deque(b)

    if len(a) < len(b):
        a, b = b, a

    for _ in range(len(a) - len(b)):
        b.appendleft('0')

    mem = 0
    for _ in range(len(a)):
        cur_sum_num = HEX.index(a.pop()) + HEX.index(b.pop()) + mem
        to_sum = cur_sum_num % 16
        mem = cur_sum_num // 16
        sum_.appendleft(HEX[to_sum])

    if mem > 0:
        sum_.appendleft(HEX[mem])

    return sum_


def mult_numbers(a, b):
    mult = deque()
    a = deque(a)
    b = deque(b)

    if len(a) < len(b):
        a, b = b, a

    for digit in range(len(b)):
        cur_multiplier = HEX.index(b.pop())
        cur_digit_num = deque()

        mem = 0
        a_tmp = deque(a)
        for _ in range(len(a)):
            cur_digit = (HEX.index(a_tmp.pop()) * cur_multiplier) + mem
            to_digit_num = cur_digit % 16
            mem = cur_digit // 16
            cur_digit_num.appendleft(HEX[to_digit_num])

        if mem > 0:
            cur_digit_num.appendleft(HEX[mem])

        for _ in range(digit):
            cur_digit_num.append('0')

        mult = add_numbers(mult, cur_digit_num)

    return mult


hex_num_a = deque(input('Введите первое шестнадцатеричное число: '))
hex_num_b = deque(input('Введите второе шестнадцатеричное число: '))



sum_a_b = add_numbers(hex_num_a, hex_num_b)
print(f'Сумма чисел = {list(sum_a_b)}')

mult_a_b = mult_numbers(hex_num_a, hex_num_b)
print(f'Произведение чисел = {list(mult_a_b)}')