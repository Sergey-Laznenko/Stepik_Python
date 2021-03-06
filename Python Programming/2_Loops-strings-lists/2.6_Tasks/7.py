"""
Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.

Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание продолжать не нужно.
"""

s = m = 0
while True:
    num = int(input())
    if (s + num) == 0:
        m += num**2
        break
    else:
        s += num
        m += num**2
print(m)
