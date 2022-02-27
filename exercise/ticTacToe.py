theBoard = {'top-L':'O','top-M':'X','top-R':'X',
            'mid-L':'X','mid-M':'O','mid-R':'O',
            'low-L':'X','low-M':'O','low-R':'X'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('-+-+-')

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for' + turn + '.Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
