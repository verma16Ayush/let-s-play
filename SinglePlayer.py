def display_board(board):
    print('\n' * 500)
    print('PLAYER IS \'O\' ')
    print('OMPUTER IS \'X\' ')
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
    if 'XXX' in ch.join(board_input) and (
            ch.join(board_input).index('XXX') == 1 or ch.join(board_input).index('XXX') == 4 or ch.join(
            board_input).index('XXX') == 7):
        return True, 'X'
    elif 'XXX' in ch.join(board_input[1::4]):
        return True, 'X'
    elif 'XXX' in ch.join(board_input[7:2:-2]):
        return True, 'X'
    elif 'OOO' in ch.join(board_input) and (
            ch.join(board_input).index('OOO') == 4 or ch.join(board_input).index('OOO') == 1 or ch.join(
            board_input).index('OOO') == 7):
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


def computer_move(available_inputs, board_input):
    score_board = {x: 0 for x in available_inputs[1::]}
    for x in available_inputs[1::]:
        mock_board_input = board_input
        score_board[x] += check_corner(x)
        score_board[x] += check_centre(x)
        score_board[x] += check_edge(x)
        mock_board_input[x] = 'X'
        if check_block(board_input) == 20:
            score_board[x] += 20
        if check_win(mock_board_input)[0]:
            score_board[x] += 100
            break
        else:
            mock_board_input[x] = ' '
    max_score_index = list(score_board.values()).index(max(list(score_board.values())))
    response = list(score_board.keys())[max_score_index]
    available_inputs.remove(response)
    # print(score_board)
    return response, available_inputs


def check_corner(x):
    if x in [1, 3, 9, 7]:
        return 3
    else:
        return 0


def check_edge(x):
    if x in [1, 2, 3, 6, 9, 8, 7, 4]:
        return 2
    else:
        return 0


def check_centre(x):
    if x == 5:
        return 10
    else:
        return 0


def check_block(board_input):
    if 'XOO' in ''.join(board_input) and (
            ''.join(board_input).index('XOO') == 1 or ''.join(board_input).index('XOO') == 4 or ''.join(
            board_input).index('XOO') == 7):
        return 20
    elif 'XOO' in ''.join(board_input[1::4]):
        return 20
    elif 'XOO' in ''.join(board_input[7:2:-2]):
        return 20
    elif 'XOO' in ''.join(board_input[1::3]) or 'XOO' in ''.join(board_input[2::3]) or 'XOO' in ''.join(
            board_input[3::3]):
        return 20
    elif 'OOX' in ''.join(board_input) and (
            ''.join(board_input).index('OOX') == 1 or ''.join(board_input).index('OOX') == 4 or ''.join(
            board_input).index('OOX') == 7):
        return 20
    elif 'OOX' in ''.join(board_input[1::4]):
        return 20
    elif 'OOX' in ''.join(board_input[7:2:-2]):
        return 20
    elif 'OOX' in ''.join(board_input[1::3]) or 'OOX' in ''.join(board_input[2::3]) or 'OOX' in ''.join(
            board_input[3::3]):
        return 20
    elif 'OXO' in ''.join(board_input) and (
            ''.join(board_input).index('OXO') == 1 or ''.join(board_input).index('OXO') == 4 or ''.join(
            board_input).index('OXO') == 7):
        return 20
    elif 'OXO' in ''.join(board_input[1::4]):
        return 20
    elif 'OXO' in ''.join(board_input[7:2:-2]):
        return 20
    elif 'OXO' in ''.join(board_input[1::3]) or 'OXO' in ''.join(board_input[2::3]) or 'OXO' in ''.join(
            board_input[3::3]):
        return 20
    else:
        return 0


def driver():
    input('WLECOME TO TIC TAC TOE \n press enter to start')
    play = True
    while play:
        board_input = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        available_inputs = ['#', 1, 2, 3, 4, 5, 6, 7, 8, 9]
        p1 = 'X'
        p2 = 'O'
        display_board(board_input)
        i = 1
        while True:
            if i % 2 == 0:
                x = int(input())
                if x in available_inputs:
                    board_input[x] = p2
                    available_inputs.remove(x)
                elif x not in available_inputs:
                    i = i - 1
                    print('invalid move. try again')
                    continue
            elif i % 2 == 1:
                x, available_inputs = computer_move(available_inputs, board_input)
                board_input[x] = p1

            win, player = check_win(board_input)
            display_board(board_input)
            if win and player == p1:
                print('computer has won')
                break
            elif win and player == p2:
                print('player has won')
                break
            elif not win and len(available_inputs) == 1:
                print('GAME TIE')
                break
            i = i + 1
        play = (bool(int(input('Do you want to play again?\n 1=yes\n 0=no: '))))


driver()
