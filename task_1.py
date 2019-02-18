#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

#https://drive.google.com/file/d/1e94azoZsxKzWZ_fC7rExDmg4FPun-vsn/view?usp=sharing

a = int(input("Введите трехзначное число: "))

b1 = a % 10
b2 = a % 100 // 10
b3 = a // 100

c = b1 + b2 + b3
d = b1 * b2 * b3

print("Сумма цифр:", c)
print("Произведение цифр:", d)
