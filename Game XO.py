# Игра крестики нолики
#--------------------------------
# Автор: Афанасьев Иван (http://github.com/Jovanni201)

board = [1,2,3,4,5,6,7,8,9]
board_size = 3
def draw_board():
    '''Выводим игровое поле'''
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)

def game_step(index, char):
    if (index > 9 or index < 1 or board[index-1] in ('X', 'O')):
        return False
    board[index-1] = char
    return True

def check_win():
    # проверяем победу одного из игроков
    win = False

    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win

def start_game():
    current_player = 'X' #текущий игрок
    step = 1 #номер шага
    draw_board()

    while (step < 10) and (check_win() == False):
        index = input('Ходит игрок ' + current_player + '. Введите номер поля (0 - выход):')

        if (index == '0'):
            break

        #Если получилось сделать шаг
        if (game_step(int(index), current_player)):
            print('Удачный ход')

            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            # увеличим номер хода
            step += 1
        else:
            print('Неверный номер! Повторите!')

    if (step == 10):
        print('Игра окончена! Ничья!')

    print('Выиграл ' + check_win())



print("Добро пожаловать в крестики нолики!")
start_game()
