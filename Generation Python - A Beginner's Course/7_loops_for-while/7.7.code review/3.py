"""
На обработку поступает последовательность из 10 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10**6
Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности и их произведение.
Если неотрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.

Найдите все ошибки в этой программе:

count = 0
p = 0
for i in range(1, 10):
    x = int(input())
    if x > 0:
        p = p * x
        count = count + 1
if count > 0:
    print(x)
    print(p)
else:
    print('NO')
"""

count = 0
p = 1
for _ in range(1, 11):
    x = int(input())
    if x >= 0:
        p *= x
        count += 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')
