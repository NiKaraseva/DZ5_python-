# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

path = r'input_encode.txt'

with open(path, 'r', encoding='UTF-8') as file:
    data = file.readline()


def Encode(string: str) -> str:
    result = ''
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            i += 1
        result += str(count) + string[i]
        i += 1
    return result


with open('output_encode.txt', 'w', encoding='UTF-8') as file:
    file.writelines(Encode(data))




