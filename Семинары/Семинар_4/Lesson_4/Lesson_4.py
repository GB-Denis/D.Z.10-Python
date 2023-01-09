# # 27 Задайте строку из набора чисел. Напишите программу, которая покажет большее и 
# # меньшее число. В качестве символа-разделителя используйте пробел.
import sympy

# some_str = input()
# int_list = list(map(int, some_str.split()))
# print(max(int_list))
# print(min(int_list))



# 28 Найдите корни квадратного уравнения Ax2 + Bx + C = 0 двумя способами
# 1) С помошью математических формул нахождения корней квадратного уравнения
# 2) С помошью дополнительных библиотек Python

# # 1)
# import math

# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# discr = pow(b, 2) - 4 * a * c
# print(f'Дискриминант = {discr}')
# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print(f'x1 = {x1} \nx2 = {x2}')
# elif discr == 0:
#     x= -b / (2 * a)
#     print(f'x = {x}') 
# else:
#     print('Корней нет')    

# # 2)
# import sympy
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# x = sympy.Symbol('x')
# print(sympy.solve(a * x ** 2 + b * x + c))



# 29 Задайте два числа. Напишите программу, которая найдёт НОК(наименьшее общее кратное) этих двух чисел

a = int(input('a = '))
b = int(input('b = '))
print(sympy.lcm(a, b))