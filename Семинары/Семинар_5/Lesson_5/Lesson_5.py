# # lambda and filter
#
# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = list(filter(lambda i: i % 2 == 0, some_list))
# print(new_list)


# # Map
# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = list(map(lambda i: i**2, some_list))
# print(new_list)


# # #Zip
# some_list = [1, 2, 3, 4, 5]
# str_list = ['one', 'two', 'three', 'four', 'five']
# print(list(zip(some_list, str_list)))


# # Enumerate
# some_list = [8, 9, 10, 0, 12]
# print(list(enumerate(some_list)))


# # ListComprehension
# some_list = [i ** 2 for i in range(1, 101) if i % 2 == 0]
# print(some_list)


# # 35 В файле находятся N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# # чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
#
# with open('twofile.txt', 'r') as file:
#     some_str = file.readline()
#
# some_list = list(map(int, some_str.split()))
# print(some_list)
#
# for i in range(1, len(some_list)):
#     if some_list[i] - 1 != some_list[i - 1]:
#         print(some_list[i] - 1)



# # 38 Напишите программу, удаляющую из текста все слова, содержащие "абв".
#
# some_text = 'фбв фблдвд абвлв адвлвл рпов фдал кенг ггео'
#
# some_text_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, some_text.split()))
# print(some_text_list)



