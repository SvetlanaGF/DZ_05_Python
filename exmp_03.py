# 3- Создайте программу для игры в ""Крестики-нолики"". 
# Для определения победы вам может пригодиться функция filter. 
# Проверяйте победу после каждого хода, фильтруя столбцы, 
# строки и диагонали по знаку хода

print('ИГРАЕМ В КРЕСТИКИ-НОЛИКИ')

board = list(range(1,10))

def draw_board(board):
    print('-' * 19)
    for i in range(3):
            print('|     |     |     |')
            print("| ", board[0+i*3], " | ", board[1+i*3], " | ", board[2+i*3], " |")
            print('|     |     |     |')
            print('-' * 19)

def take_choice(player_XO):
    valid = False
    while not valid:
        choice = int(input(f"В какую клетку поставите {player_XO} ? "))
        if choice >= 1 and choice <= 9:
            if(str(board[choice-1]) not in "XO"):
                board[choice-1] = player_XO
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Введите число от 1 до 9!")

def check_win(board):
    win_choice = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_choice:
        if board[each[0]] == board[each[1]] == board[each[2]]:
           return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_choice("X")
        else:
           take_choice("O")
        counter += 1
        if counter > 4:
           who_win = check_win(board)
           if who_win:
                draw_board(board)
                print(who_win, "победил!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
main(board)