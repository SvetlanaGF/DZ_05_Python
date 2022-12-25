# 2- Создайте программу для игры с конфетами человек против человека.
# a) Добавьте игру против бота

from random import randint as ri

total_candy = ri(29,250)
take_candy = 0

def turn_order():
    """Определяем очередность хода"""
    random_move = ri(1,2)
    if random_move == 1:
        print('Первый ход у Игрока.')
        player_turn()
    else:
        print('Первый ход у бота.')
        bot_turn()

def player_turn():
    global total_candy
    global take_candy
    """Игрок в свой ход берет конфеты"""
    print(f'\nХод Игрока. На столе {total_candy} конфет')
    take_candy = int(input('Сколько конфет возьмете? (от 1 до 28): '))
    while take_candy > 28 or take_candy == 0 or take_candy > total_candy:
        take_candy = int(input('Конфет можно взять от 1 до 28. Сколько возьмете? '))
    total_candy -= take_candy

    if total_candy > 0:
        bot_turn()
    else:
        print('ПОБЕДА! Бот проиграл.')

def bot_turn():
    global total_candy
    global take_candy
    """Бот в свой ход берет конфеты"""
    take_candy = ri(1, 28)
    total_candy -= take_candy
    print(f'\nХодит Бот.\nБот взял {take_candy} конфет. Осталось {total_candy} конфет')
    
    if total_candy > 0:
        player_turn()
    else:
        print('Победа БОТа! Вы проиграли.')

print(f'На столе {total_candy} конфет.\nЗа один ход можно взять от 1 до 28 конфет.\nКто взял последнюю конфету, тот выиграл!\nЖребий определит, чей ход первый:')
turn_order()