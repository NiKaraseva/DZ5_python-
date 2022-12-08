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
        PlayerTurn()

