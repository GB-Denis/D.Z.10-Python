# # # Задание 17. Задайте список из N элементов, заполненный числами из промежутка [-N,N].
# # #  Найдите поизведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

# import random
# n = int(input('Введите количество элементов: '))
# mult = 1
# some_list = [random.randint(-n, n) for _ in range(n)]
# print(some_list)
# with open('file.txt', 'w', encoding='utf-8') as file:
#     count = random.randint(1, n)
#     for _ in range(count):
#         file.write(f'{random.randint(0, n - 1)}' + '\n')
# with open('file.txt', 'r', encoding='utf-8') as file:
#     index_list = file.read().splitlines()
#     for index in index_list:
#         mult = mult * some_list[int(index)]
# print(mult)




# # Введите кол-во строк, потом строки. Строки должны записаться в текстовый файл. 
# # После вводим число, если есть число в файле, то написать ДА.
# a = int(input('Введите количество строк: '))
# with open('file.txt', 'w', encoding='utf-8') as file:
#     for _ in range(a):
#         file.write(input() + '\n')
# c = input('Введитие искомое число ')
# with open('file.txt', 'r', encoding='utf-8') as file:
#     strings = file.read().splitlines()
#     count=0
#     b = False
#     for line in strings:
#         count +=1
#         if c in line:
#             b = True
#             print(f'DA -> {count}')
#     if not b:
#         print('NET')    



# # Напишите функцию, которая принимает номер месяца и язык (русский или английский), а возвращает его название.
#     # Ввод: print(month_name(3, "en"))
#     # March
#     # Ввод: print(month_name(3, "ru"))
#     # Март

# def mounth(x,y):
#     listEn = ('January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December')
#     listRu = ('Январь' , 'Февраль' , 'Март' , 'Апрель' , 'Май' , 'Июнь' , 'Июль' , 'Август' , 'Сентябрь' , 'Октябрь' ,'Декабрь')
#     if x > 0 and x < 13:
#         if y == 'en':
#             return(listEn[x-1])
#         if y == 'ru':
#             return(listRu[x-1])
# print(mounth(10, 'ru'))  




# # Напишите программу которая определит позицию второго вхождения строки в списке либо сообщит что её нет
# # ['qwe' , 'asd' , 'zxc' , 'z' , 'ertqwe'] -> Ответ 3
# some_list = ['qwe' , 'asd' , 'zxc' , 'z' , 'ertqwe']
# a = input('Введите искомое ')
# count = 0
# count2 = 0
# b = False
# for line in some_list:
#     count +=1
#     if a ==line:
#         count2 += 1
#         if count2 == 2:
#             b = True
#             print(f'{count} ')
#             break
# if not b:
#     print('NET')        
