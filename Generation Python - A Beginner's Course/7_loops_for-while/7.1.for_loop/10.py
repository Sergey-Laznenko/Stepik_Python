"""
На вход программе подается три натуральных числа m, p, n:
- m: стартовое количество организмов;
- p: среднесуточное увеличение в %;
- n: количество дней для размножения.

Напишите программу, которая предсказывает размер популяции организмов.
Программа должна выводить размер популяции в каждый день, начиная с 11 и заканчивая nn-м днем.
"""

m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, m)
    m = m + m * p / 100
