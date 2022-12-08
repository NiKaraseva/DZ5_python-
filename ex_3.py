# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

path = r'input1.txt'

with open(path, 'r', encoding='UTF-8') as file:
    string = file.readline()

print(string)

# string = list(string)
#
# count = 0
# for i in range(len(string)):
#     result = ''
#     if string[i] == [string[i + 1]]:
#         count = + 1
#     result = f'{count} + {string[i]}'
# print(result)



