"""
Напишите программу, которая определяет, является ли год с данным номером високосным.
Если год является високосным, то выведите «YES», иначе выведите «NO».
"""

x = int(input())
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print('YES')
else:
    print('NO')
