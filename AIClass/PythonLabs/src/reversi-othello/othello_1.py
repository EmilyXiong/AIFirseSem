
# pzl = 'XX.OO.XO.'
pzl = '...........................ox......xo...........................'

EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'Black', WHITE: 'White'}

UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

def printPuzzle (pzl):
    print ("\n+___+___+___+___+___+___+___+___+")   
    for row in range(0,8):
        line = '|'
        for i in range(0, 8):
            line = line + " " + pzl[int(row*8) + i]  + " |" 
        print (line)
        print ("+___+___+___+___+___+___+___+___+")  
            
def whoMoveNext(pzl):
    if sum(j=='x' for j in pzl) <= sum(j=='O' for j in pzl):
        return 'x'
    else:
        return 'o'

def squares():
    return [i for i in range(11, 89) if 1 <= (i % 10) <= 8]

def initial_board():
#
    board = [OUTER] * 100
    for i in squares():
        board[i] = EMPTY
        
    board[44], board[45] = WHITE, BLACK
    board[54], board[55] = BLACK, WHITE
    return board

def print_board(board):
#
    rep = ''
    rep += '  %s\n' % ' '.join(map(str, range(1, 9)))
    for row in range(1, 9):
        begin, end = 10*row + 1, 10*row + 9
        rep += '%d %s\n' % (row, ' '.join(board[begin:end]))
    return rep


def is_valid(move):
    return isinstance(move, int) and move in squares()

def opponent(player):
    return BLACK if player is WHITE else WHITE


def find_bracket(square, player, board, direction):
#
    bracket = square + direction
    if board[bracket] == player:
        return None
    opp = opponent(player)
    while board[bracket] == opp:
        bracket += direction
    return None if board[bracket] in (OUTER, EMPTY) else bracket




board = print_board (initial_board())
print(board)

# printPuzzle(pzl)
# print(squares())
# print(nextMove(pzl))



# print( whoMove(pzl))
# print(emptyPosition(pzl))
# alradyMoved = False
# good, bad, tie = partitionMoves(pzl, alradyMoved, nextMove(pzl))
# print("good set:", good)
# print("bad set:", bad)
# print("tie set:", tie)
