import random as rd


def display_board(board):
    print('\n' * 500)
    print(' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9] + ' ')
    print('   ' + '|' + '   ' + '|' + '   ')
    print('___________')
    print(' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6] + ' ')
    print('   ' + '|' + '   ' + '|' + '   ')
    print('___________')
    print(' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3] + ' ')
    print('   ' + '|' + '   ' + '|' + '   ')


ch = ''


def take_input():
    p1 = input('player 1 choose \'X\' or \'O\': ').upper()
    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'
    return p1, p2


def check_win(board_input):
    if 'XXX' in ch.join(board_input) and (ch.join(board_input).index('XXX')==1 or ch.join(board_input).index('XXX')==4 or ch.join(board_input).index('XXX')==7):
        return True, 'X'
    elif 'XXX' in ch.join(board_input[1::4]):
        return True, 'X'
    elif 'XXX' in ch.join(board_input[7:2:-2]):
        return True, 'X'
    elif 'OOO' in ch.join(board_input)and (ch.join(board_input).index('OOO')==4 or ch.join(board_input).index('OOO')==1 or ch.join(board_input).index('OOO')==7):
        return True, 'O'
    elif 'OOO' in ch.join(board_input[1::4]):
        return True, 'O'
    elif 'OOO' in ch.join(board_input[7:2:-2]):
        return True, 'O'
    elif 'OOO' in ch.join(board_input[1::3]) or 'OOO' in ch.join(board_input[2::3]) or 'OOO' in ch.join(
            board_input[3::3]):
        return True, 'O'
    elif 'XXX' in ch.join(board_input[1::3]) or 'XXX' in ch.join(board_input[2::3]) or 'XXX' in ch.join(
            board_input[3::3]):
        return True, 'X'
    else:
        return False, 'y'


def driver():
    print('WELCOME TO TIC TAC TOE')
    play = True
    while play:
        board_input = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        available_inputs = ['#', 1, 2, 3, 4, 5, 6, 7, 8, 9]
        p1, p2 = take_input()
        display_board(board_input)
        for i in range(1, 11, 1):
            x = int(input())
            if x not in available_inputs:
                print('invalid input. place already occupied. try again.')
                i -= 1
                continue
            if i % 2 == 0 and x in available_inputs:
                board_input[x] = p2
                available_inputs.pop(available_inputs.index(x))
            elif i % 2 != 0 and x in available_inputs:
                board_input[x] = p1
                available_inputs.pop(available_inputs.index(x))
            win, player = check_win(board_input)
            display_board(board_input)
            if win and player == p1:
                print('player 1 has won ')
                break
            elif win and player == p2:
                print('player 2 has won')
                break
            elif not win and len(available_inputs)==1:
                print('Game tie.')
                break
        play = (bool(int(input('Do you want to play again?\n 1=yes\n 0=no: '))))


driver()
