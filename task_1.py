# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.


MIN_NATURAL_NUM = 2
MAX_NATURAL_NUM = 99


START_CHECK_NUM = 2
END_CHECK_NUM = 9

if MIN_NATURAL_NUM <= MAX_NATURAL_NUM and START_CHECK_NUM <= END_CHECK_NUM:
    answer = [0 for _ in range(START_CHECK_NUM, END_CHECK_NUM + 1)]


    for natural_num in range(MIN_NATURAL_NUM, MAX_NATURAL_NUM + 1):
        for check_num in range(START_CHECK_NUM, END_CHECK_NUM + 1):
            if natural_num % check_num == 0:
                answer[check_num - START_CHECK_NUM] = answer[check_num - START_CHECK_NUM] + 1


    print(f'В диапазоне натуральных чисел от {MIN_NATURAL_NUM} до {MAX_NATURAL_NUM}: ')
    for check_num in range(START_CHECK_NUM, END_CHECK_NUM + 1):
        print(f'Числу {check_num} кратно чисел: {answer[check_num - START_CHECK_NUM]}')

else:
    print('Некорректные диапазоны!')
