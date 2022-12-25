# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# Человек против человека

from random import randint as ri

def turn_order():
    """Определяем очередность хода"""
    random_move = ri(1,2)
    if random_move == 1:
        print('Первый ходит Игрок 1!')
        player_turn(1)
    elif random_move == 2:
        print('Первый ходит Игрок 2!')
        player_turn(2)
    

def take_sweet(player, leftover_sweet):
    """Игрок в свой ход берет конфеты"""
    print(f'\nХод Игрока {player}. На столе {leftover_sweet} конфет')
    take_candy = int(input('Сколько конфет возьмете? (от 1 до 28) '))
    while take_candy > 28 or take_candy < 0 or take_candy > leftover_sweet:
        take_candy = int(input('Конфет можно взять от 1 до 28. Сколько возьмете? '))
    return take_candy

def active_player(active):
    """Ход переходит к другому игроку"""
    if active == 1: active = 2
    else: active = 1
    return active

def player_turn(whose_move):
    """Начинаем игру"""
    total_candy = ri(29, 101)
    take_candy = 0
    print(f'На столе {total_candy} конфет.\nЗа один ход можно взять от 1 до 28 конфет.\nКто взял последнюю конфету, тот выиграл!\nЖребий определит, чей ход первый:')
    while total_candy > 0:
        take_candy = take_sweet(whose_move, total_candy)
        total_candy -= take_candy
    
        if total_candy == 0: print(f'Конфеты закончились!    Победитель игрок {whose_move}!')
        
        whose_move = active_player(whose_move)

turn_order()
