"""
На вход программе подается одно вещественное число x измеряемое в градусах.
Программа должна вывести одно число – значение тригонометрического выражения.
"""

from math import *
a = float(input())
r = ((a * pi) / 180)
print(sin(r) + cos(r) + tan(r)**2)
