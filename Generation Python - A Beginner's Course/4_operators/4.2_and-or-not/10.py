"""
Напишите программу, которая принимает целое число xx и определяет,
принадлежит ли данное число указанным промежуткам.
"""

x = int(input())
if (-30 < x) and (x <= -2) or (7 < x) and (x <= 25):
    print('Принадлежит')
else:
    print('Не принадлежит')