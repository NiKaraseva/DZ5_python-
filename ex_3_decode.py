path = r'input_decode.txt'

with open(path, 'r', encoding='UTF-8') as file:
    data = file.readline()


def Decode(string: str) -> str:
    result = ''
    count = ''
    for item in string:
        if item.isdigit():
            count += item
        else:
            result += item * int(count)
            count = ''
    return result


with open('output_decode.txt', 'w', encoding='UTF-8') as file:
    file.writelines(Decode(data))

