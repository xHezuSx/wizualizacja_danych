# tic tac toe
# zrobimy to na listach
# plansza będzie składała się listy o nazwie PLANSZA, będzie ona składała się z 3 podlist co daje w sumie 9 pól tak jak w kółku i krzyrzyk
# wyświetlanie całej planszy będzie się odbywało na początku oraz za każdym razem gdy użytkowik wpisze wartości
# użytkownik wpisywał będzie numer wiersza a następnie numer kolumny pola które będzie kolejno uzupełniane odpowiednimi wartościami O/X
# sprawdzanie wygranej będzie odbywało się po przez sprawdzenie czy którekolwiek X/O będzie na jakimkowiek boku lub przekątnej, jeśli plansza będzie pełna gra zakończy się remisem
# program zapyta o ponowną grę

# rozbuduj program wprowadzając grę z komputerem

BOARD = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
def display_board(board):
    for row in board:
        row.insert(1, ' | ')
        row.insert(3, ' | ')
        for field in row:
            print(field, end='')
        if row != board[-1]:
            print('\n---------')
        del row[3]
        del row[1]

def row_input():
    print('')
    while True:
        try:
            row = int(input('type row: '))
            if row < 1 or row > 3:
                print('type a row number between 1 and 3')
            if (1 <= row <= 3):
                return row
        except:
            print('type a row number between 1 and 3')

def column_input():
    while True:
        try:
            column = int(input('type column: '))
            if column < 1 or column > 3:
                print('type a column number between 1 and 3')
            if (1 <= column <= 3):
                return column
        except:
            print('type a column number between 1 and 3')

def insert_to_board(board, row_numb, column_numb, sign):
    row_numb = row_numb-1
    column_numb = column_numb-1
    row = board[row_numb]
    if row[column_numb] == ' ':
        row[column_numb] = sign
        return False
    else:
        return True

def check_win(board):
    for row in board:       # every horizontal line
        X = row.count('X')
        O = row.count('O')
        if X == 3 or O == 3:
            return True

    for i in range(3):      # every vertical line
        side = []
        for row in board:
            if row[i] != ' ':
                side.append(row[i])
        if side.count('X') == 3 or side.count('O') == 3:
            return True

    l_cross = []            # cross from left
    itr = 0
    for row in board:
        l_cross.append(row[itr])
        itr += 1
    l_X = l_cross.count('X')
    l_O = l_cross.count('O')
    if l_X == 3 or l_O == 3:
        return True

    r_cross = []            # cross from right
    itr = 2
    for row in board:
        r_cross.append(row[itr])
        itr -= 1
    r_X = r_cross.count('X')
    r_O = r_cross.count('O')
    if r_X == 3 or r_O == 3:
        return True

    return False

def check_draw(board):
    for rows in board:
        for field in rows:
            if field == ' ':
                return False
    return True

                            #GAME
counter = 0
x_score = 0
o_score = 0
run = True
while run:
    counter += 1
    sign = ''
    if counter % 2 == 0:
        sign = 'O'
    else:
        sign = 'X'

    print('\n -->', sign, 'turn')
    display_board(BOARD)
    print('\n -->', sign, 'turn')
    row = row_input()
    column = column_input()

    while insert_to_board(BOARD, row, column, sign):
        print("you can't insert -->", sign, ' this field is already filled')
        row = row_input()
        column = column_input()

    while check_win(BOARD):
        display_board(BOARD)
        print('\n\t\t\t\t\tWINNER -->', sign,'\n\n')
        if sign == 'O':
            o_score += 1
        elif sign == 'X':
            x_score += 1
        print('\n\t -- SCORE -- \nX:',x_score,'\nO:',o_score )
        play_again = input('do you wanna play again? ([y]/n) --> ')
        if play_again.lower() == 'y' or play_again.lower() == 'yes':
            BOARD = [
                [' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']
            ]
            break
        print('\t\t\t\t --> thanks for playing')
        run = False
        break

    while check_draw(BOARD):
        display_board(BOARD)
        print('\n\t\t\t\t\t --> DRAW\n\n')
        print('\n\t\t\t\t\t -- SCORE --  \nX:', x_score, '\nO:', o_score)
        play_again = input('do you wanna play again? ([y]/n)')
        if play_again.lower() == 'y' or play_again.lower() == 'yes':
            BOARD = [
                [' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']
            ]
            break
        print('\t\t\t\t\t\t --> thanks for playing')
        run = False
        break