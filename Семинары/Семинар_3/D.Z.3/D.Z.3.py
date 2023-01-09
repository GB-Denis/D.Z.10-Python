# # 22 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# #  стоящих на нечётной позиции

# from random import randint
# some_list = [randint(1, 10) for _ in range(5)]
# summa = 0
# print(some_list)
# for idx in range(0, len(some_list), 2):
#     summa += some_list[idx]
# print(summa)    



# # 23 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# # первый и последний элемент, второй и предпослений и т.д.

# from random import randint
# some_list = [randint(1, 10) for _ in range(5)]
# new_list = []
# print(some_list)
# for i in range(0, (len(some_list) - 1) // 2 + 1):
#     new_list.append(some_list[i] * some_list[len(some_list) - 1 - i])
# print(new_list)    


# 24 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и мминимальным значением дробной части элементов

# some_list = [float(input()) for _ in range(int(input()))]
# min = 1
# max = 0
# for el in some_list:
#     if el % 1 < min and el % 1 != 0:
#         min = el % 1
#     else:
#         if el % 1 > max:
#             max = el % 1
# print (max, min)            
# print(max - min)   

# ИЛИ

# some_list = [input() for _ in range(int(input()))]
# min = 1
# max = 0
# for el in some_list:
#     if '.' in el:
#         if float('0.' + el.split('.')[1]) < min:
#             min = float('0.' + el.split('.')[1])
#         else: 
#             if float('0.' + el.split('.')[1]) > max:
#                 max = float('0.' + el.split('.')[1])
# print(max - min)     



# # 25 Напишите программу, которая будет преобразовывать десятичное число в двоичное 
# n = int(input())
# out_str = ''
# while n != 0:
#     out_str = str(n % 2) + out_str
#     n //= 2
# print(out_str)    


# # 26 Задайте число, Составьте список чисел Фибоначчи, в том числе 
# # для отрицательных индексов

# k = int(input())
# some_list = [0] * (2 * k + 1)
# some_list[k + 1] = 1
# for i in range(k + 2, 2 * k + 1):
#     some_list[i] = some_list[i - 1] + some_list[i - 2]
# for i in range(k - 1, -1, -1):
#     some_list[i] = some_list[i + 2] - some_list[i + 1]   
# print(some_list)
