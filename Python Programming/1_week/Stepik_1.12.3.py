"""
Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
первое число, второе число и операцию, после чего применяет операцию к введённым числам
("первое число" "операция" "второе число") и выводит результат на экран.
"""

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = input('Введите операцию (+,-,/,*,mod,div,pow): ')

if (b == 0 and c in('mod', '/', 'div')):
    print('Деление на 0!')
elif c == '+':
    print(f'Результат: ', a + b)
elif c == '-':
    print(f'Результат: ',a - b)
elif c == '*':
    print(f'Результат: ',a * b)
elif c == '/':
    print(f'Результат: ',a / b)
elif c == 'mod':
    print(f'Результат: ',a % b)
elif c == 'pow':
    print(f'Результат: ',a ** b)
elif c == 'div':
    print(f'Результат: ',a // b)
else:
    print('НЕ верно введённые данные')