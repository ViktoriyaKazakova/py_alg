#2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

a = 5
print("%d = %s" % (a, bin(a)))

b = 6
print("%d = %s" % (b, bin(b)))

print("%d & %d = %d (%s)" % (a, b, a & b, bin(a & b)))
print("%d | %d = %d (%s)" % (a, b, a | b, bin(a | b)))
print("%d ^ %d = %d (%s)" % (a, b, a ^ b, bin(a ^ b)))
print("%d << 2 = %d (%s)" % (a, a << 2, bin(a << 2)))
print("%d >> 2 = %d (%s)" % (a, a >> 2, bin(a >> 2)))