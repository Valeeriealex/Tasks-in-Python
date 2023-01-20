#Количество клеток
board_size = 3

#Игровое поле
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Вывод на печать поля
def print_board():
    print(('_' * 4 * board_size))
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board [i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)
    
#Проверка победы одного из игроков
def check_win():
    win = False
    win_combo = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7,), (2, 5, 8,),
        (0, 4, 8), (2, 4, 6)
    )
    for pos in win_combo:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] and board[pos[1]] in ('x','o')):
            win = board[pos[0]]
    return win

#Ход игроков
def game_step(index, char):
    if (index > 9 or index < 1 or board[index-1] in ('x', 'o')):
        return False
    board[index-1] = char
    return True


#Запуск игры
def start_game():
    current_player = 'x'
    step = 1
    print_board()

    while (step<10) and (check_win() == False):
        index = input('Ходит игрок ' + current_player + '. Введите номер поля: ')
        if (index == '0'):
           break
        if (game_step(int(index), current_player)):
            print('Ход сделан!') 
            if(current_player == 'x'):
                current_player = 'o'
            else:
                current_player = 'x'
            print_board()
            step +=1
        else:
            print('Введины некорректные данные! Повторите!')  
    if (step == 10):
        print('Игра окончена. Ничья!')
    else:
        print('Выиграл ' + check_win())
 
print('Начните игру в крестики-нолики!')
start_game()