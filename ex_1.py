# 1. Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""

from random import randint as rnd

total_sweets = 150
player_sweets = 0
bot_sweets = 0
take_sweets = 0


def FirstMove():
    draw = rnd(0, 1)
    print(f'Жребий = {draw}')
    if draw == 0:
        PlayerTurn()
    else:
        BotTurn()


def PlayerTurn():
    global take_sweets
    global total_sweets
    global player_sweets
    take_sweets = int(input(f'На столе сейчас {total_sweets}. Сколько конфет вы хотите взять? '))
    while take_sweets > total_sweets or take_sweets > 28 or take_sweets <= 0:
        take_sweets = int(input('Вы играете не по правилам! Возьмите количество конфет от 1 до 28: '))
    total_sweets -= take_sweets
    player_sweets += take_sweets
    if total_sweets > 0:
        BotTurn()
    else:
        print('Поздравляю! Вы победили!')


def BotTurn():
    global take_sweets
    global total_sweets
    global bot_sweets
    if total_sweets % 29 != 0:
        take_sweets = total_sweets % 29
    else:
        take_sweets = rnd(1, 28)
    total_sweets -= take_sweets
    bot_sweets += take_sweets
    print(f'Бот взял {take_sweets} конфет.')
    if total_sweets > 0:
        PlayerTurn()
    else:
        print('Бот красавчик!')

FirstMove()