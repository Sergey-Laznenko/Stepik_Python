"""
На вход программе подается натуральное число nn, а затем nn строк. Напишите программу,
которая создает из указанных строк список и выводит его.
"""

data = list()
for _ in range(int(input())):
    data.append(input())
print(data)