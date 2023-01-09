# # 30 Вычислить число с заданной точностью d
#
# from math import pi
#
# d = input()
# accur = len(d)
# print (str(pi)[0:accur])



# # 31 Задайте неправильное число N. Напишите программу, которая составит список простых множителей числа N.
#
# n = int(input())
# if n == 1:
#     print(1)
# some_list = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         for j in range(2, i // 2 + 1):
#             if i % j == 0:
#                 break
#         else:
#             some_list.append(i)
# print(*some_list, sep=', ')



# # 32 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# # элементов исходной последовательности.
#
# number_set = set()
# out_list = []
# some_list = list(map(int, input().split()))
# for ind in range(0, len(some_list)):
#     if some_list[ind] not in number_set:
#         number_set.add(some_list[ind])
#         for ind1 in range(ind + 1, len(some_list)):
#             if some_list[ind] == some_list[ind1]:
#                 break
#         else:
#             out_list.append(some_list[ind])
# print(out_list)

# ИЛИ

# some_list = list(map(int, input().split()))
# for i in some_list:
#     if some_list.count(i) ==1:
#         print(i, end=' ')




