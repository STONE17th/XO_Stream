import random

WIN_CONDITION = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (2, 5, 8), (0, 4, 8),
                 (1, 4, 7), (2, 4, 6))

# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
board = [str(i) for i in range(1, 10)]
mark = "O"


def switch_mark():
    global mark
    if mark == 'X':
        mark = 'O'
    else:
        mark = 'X'


def enemy_mark():
    global mark
    if mark == 'X':
        return 'O'
    else:
        return 'X'


def show_board(board: list):
    print(f'\n{board[0]:^3}║{board[1]:^3}║{board[2]:^3}')
    print('═══╬═══╬═══')
    print(f'{board[3]:^3}║{board[4]:^3}║{board[5]:^3}')
    print('═══╬═══╬═══')
    print(f'{board[6]:^3}║{board[7]:^3}║{board[8]:^3}')


def game():
    while any(list(map(lambda x: x.isdigit(), board))) and not check_win():
        switch_mark()
        show_board(board)
        turn = play_turn() if mark == 'X' else bot_turn(board)
        board[turn] = mark
    show_board(board)
    if check_win():
        print(f'\nПоздравляем победа за {mark}')
    else:
        print('\nЁбанные бараны у вас ничья! НИЧЬЯ, Карл!')


def bot_turn(board: list) -> int:
    if board[4].isdigit():
        return 4
    else:
        turn = pre_win(board, mark)
        enemy_turn = pre_win(board, enemy_mark())
        if turn:
            return turn
        elif enemy_turn:
            return enemy_turn
        else:
            while any(list(map(lambda x: board[x].isdigit(), [0, 2, 6, 8]))):
                turn = random.choice([0, 2, 6, 8])
                if board[turn].isdigit():
                    return turn
            while True:
                turn = random.randint(0, 8)
                if board[turn].isdigit():
                    return turn


def pre_win(board: list, cur_mark: str) -> int:
    for win in WIN_CONDITION:
        if (board[win[0]] == board[win[1]] == cur_mark) and board[win[2]].isdigit():
            return win[2]
        elif board[win[1]] == board[win[2]] == cur_mark and board[win[0]].isdigit():
            return win[0]
        elif board[win[0]] == board[win[2]] == cur_mark and board[win[1]].isdigit():
            return win[1]
    return False


def check_win():
    for win in WIN_CONDITION:
        if board[win[0]] == board[win[1]] == board[win[2]]:
            return True
    return False


def play_turn() -> int:
    while True:
        turn = input(f'\n{mark} - Делайте ваш ход: ')
        if turn.isdigit() and 0 < int(turn) < 10 and board[int(turn) - 1].isdigit():
            return int(turn) - 1


if __name__ == '__main__':
    game()
