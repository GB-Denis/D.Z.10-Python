# # 38 Напишите программу, удаляющую из текста все слова, содержащие "абв".
#
# some_text = 'фбв фблдвд абвлв адвлвл рпов фдал кенг ггео'
#
# some_text_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, some_text.split()))
# print(some_text_list)


# # 39 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# # Входные и выходные данные хранятся в отдельных текстовых файлах.
#
# def press(file, result):
#     with open(file, 'r', encoding='utf-8') as text:
#         with open(result, 'w', encoding='utf-8') as res:
#             inp_str = text.readline()
#             ind = 0
#             out_str = ''
#             count = 1
#             while ind < len(inp_str) - 1:
#                 if inp_str[ind] == inp_str[ind + 1]:
#                     count += 1
#                 else:
#                     if count == 1:
#                         res.write(inp_str[ind])
#                     else:
#                         res.write(str(count) + inp_str[ind])
#                     count = 1
#                 ind += 1
#             print(out_str)
#
#
# # press('file.txt', 'result.txt')
#
#
# def depress(file, result):
#     with open(file, 'r', encoding='utf-8') as text:
#         with open(result, 'w', encoding='utf-8') as res:
#             inp_str = text.readline()
#             count = ''
#             for letter in inp_str:
#                 if letter.isdigit():
#                     count += letter
#                 else:
#                     if count != '':
#                         res.write(int(count) * letter)
#                     else:
#                         res.write(letter)
#                     count = ''
#
#
# depress('result.txt', 'result_2.txt')



