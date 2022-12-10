# 2. Создайте программу для игры в ""Крестики-нолики"".
import random
from random import randint as rnd

def PrintField(field: list):

    print(f' {field[0]} | {field[1]} | {field[2]} ')
    print('–––––––––––')
    print(f' {field[3]} | {field[4]} | {field[5]} ')
    print('–––––––––––')
    print(f' {field[6]} | {field[7]} | {field[8]} ')


array = list(range(1, 10))
x = chr(10060)
o = chr(11093)
win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

def StartGame():
    first_move = rnd(0, 1)
    if first_move == 0:
        PlayerTurn(x, array)
    else:
        BotTurn(o, array)


def PlayerTurn(simb: str, field: list):
    while True:
        move = int(input('Ваш ход, мистер х:'))
        if move in field:
            field[move - 1] = simb
            PrintField(field)
            if CheckWin(x, array):
                print('Вы великолепны! Человек победил бота!')
                break
            elif CheckDraw(array):
                print('Увы, ничья!')
                break
            else:
                BotTurn(o, field)
        else:
            print('Неверный ход! Попробуйте ещё раз :)')
            continue



def BotTurn(simb: str, field: list):
    global win
    while True:
        if field[4].isdigit():
            field[4] = simb
        else:
            corner = [0, 2, 6, 8]
            random.shuffle(corner)
            for opt in win:
                if (field[opt[0]] == field[opt[1]] == simb) and field[opt[2]].isdigit():
                    field[opt[2]] = simb
                elif (field[opt[1]] == field[opt[2]] == simb) and field[opt[0]].isdigit():
                    field[opt[0]] = simb
                elif (field[opt[0]] == field[opt[2]] == simb) and field[opt[1]].isdigit():
                    field[opt[1]] = simb
            for opt in win:
                if (field[opt[0]] == field[opt[1]] != simb) and field[opt[2]].isdigit():
                    field[opt[2]] = simb
                elif (field[opt[1]] == field[opt[2]] != simb) and field[opt[0]].isdigit():
                    field[opt[0]] = simb
                elif (field[opt[0]] == field[opt[2]] != simb) and field[opt[1]].isdigit():
                    field[opt[1]] = simb
            for cell in corner:
                if field[cell].isdigit():
                    field[cell] = simb
                    break
            else:
                turn = random.randint(1, 9)
                if field[turn].isdigit():
                    field[turn] = simb
                    break
        PrintField(array)
        if CheckWin(o, array):
            print('Бот выиграл!')
            break
        elif CheckDraw(array):
            print('Увы, ничья!')
            break
        else:
            PlayerTurn(x, array)



def CheckWin(simb: str, field: list):
    global win
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



StartGame()

