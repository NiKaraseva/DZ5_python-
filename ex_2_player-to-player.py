# 2. Создайте программу для игры в ""Крестики-нолики"".

from random import randint as rnd


def PrintField(field: list):

    print(f' {field[0]} | {field[1]} | {field[2]} ')
    print('–––––––––––')
    print(f' {field[3]} | {field[4]} | {field[5]} ')
    print('–––––––––––')
    print(f' {field[6]} | {field[7]} | {field[8]} ')


def Game():
    array = list(range(1, 10))
    x = chr(10060)
    o = chr(11093)
    first_move = rnd(0, 1)
    if first_move == 0:
        xo = x
    else:
        xo = o
    PrintField(array)

    while True:
        move = int(input(f'Ход {xo}: '))
        if move in array:
            array[move - 1] = xo
            PrintField(array)
            if CheckWin(xo, array):
                print(f'Поздравляем, {xo} красавчик!')
                break
            elif CheckDraw(array):
                print(f'НИЧЬЯ!')
                break
            xo = x if xo == o else o
        else:
            print('Неверный ход, попробуйте ещё раз!')
            continue


def CheckWin(simb: str, field: list):
    win = ((0, 1, 2), (3, 4, 5,), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win:
        for j in i:
            if field[j] == simb:
                continue
            else:
                break
        else:
            return True
    else:
        return False


def CheckDraw(field: list):
    for i in range(1, 10):
        if i in field:
            return False
    return True

Game() 