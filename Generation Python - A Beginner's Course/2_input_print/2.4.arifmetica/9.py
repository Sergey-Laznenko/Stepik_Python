"""
Напишите программу, которая считывает целое число,
после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.
"""

num = int(input())
print(f'Следующее за числом {num} число: {num + 1}')
print(f'Для числа {num} предыдущее число: {num - 1}')
