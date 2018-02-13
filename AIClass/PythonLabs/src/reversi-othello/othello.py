import sys


DIRECTIONS = {'L':[0, -1], 'R': [0, 1], 'U':[-1, 0], 'D':[1, 0],
              'UL':[-1, -1], 'UR':[-1, 1], 'DL':[1, -1], 'DR':[1, 1]}

COUNTER_DIRECTIONS = {'L':[0, 1], 'R': [0, -1], 'U':[1, 0], 'D':[-1, 0],
              'UL':[1, 1], 'UR':[1, -1], 'DL':[-1, 1], 'DR':[-1, -1]}

def printPuzzle (pzl):
    print ("\n  a b c d e f g h")  
    for row in range(0,8):
        line = str(row)
        for i in range(0, 8):
            line = line + " " + pzl[int(row*8) + i] 
        print (line)

def opponent(player):
    return 'o' if player is 'x' else 'x'

def findAllOpponentPos(pzl, player):
    oppo = opponent(player)
    return [i for i in range(64) if pzl[i] == oppo]

def getRowCol(pos):
    return int(pos/8), int(pos%8)

def getPos(row, col):
    return int(row*8 + col)

def findAllMoves(pzl, player):
    positions = set()
    oppoentTiles = findAllOpponentPos(pzl, player)
    for pos in oppoentTiles:
        if pos == 16:
            print ("11")
        row, col = getRowCol(pos)
        for dir in DIRECTIONS:
            nbrRow = DIRECTIONS[dir][0]+row
            nbrCol = DIRECTIONS[dir][1]+col
            if nbrRow >=0 and nbrRow < 8 and nbrCol >= 0  and nbrCol < 8:
                nbrPos =  getPos(nbrRow, nbrCol)
                if  pzl[nbrPos] == '.' and isValidPos(pzl, player, nbrRow, nbrCol, dir):
                    positions.add(nbrPos)
    return positions


def isValidPos(pzl, player, row, col, dir):
    newRow = row + COUNTER_DIRECTIONS[dir][0]
    newCol = col + COUNTER_DIRECTIONS[dir][1]
    while newRow >=0 and newRow < 8 and newCol>=0 and newCol < 8:
        title = pzl[getPos(newRow, newCol)] 
        if title == '.':
            return False
        elif title == player:
            return True
        else:
            newRow = newRow + COUNTER_DIRECTIONS[dir][0]
            newCol = newCol + COUNTER_DIRECTIONS[dir][1]
    return False
    
player = 'o'
pzl = '...........................ox......xo...........................'
   
if len(sys.argv) > 2:
    pzl = sys.argv[1]
    player = sys.argv[2]
    if player == 'X':
        player = 'x'
    elif player == 'O':
        player = 'o'
elif len(sys.argv) == 2:
    pzl = sys.argv[1]
    if pzl.count('.') % 2:
        player = 'o'
    else:
        player = 'x'
newPzl=''
for ch in pzl:
    if ch == 'X':
        newPzl = newPzl+'x'
    elif ch=='O':
        newPzl=newPzl+'o'
    else:
        newPzl=newPzl+ch
pzl = newPzl
print("puzzl = '" + pzl + "'   player=" + player)
allMoves = findAllMoves(pzl, player)
for pos in allMoves:
    pzl = pzl[:pos] + '*' + pzl[pos+1:]
print("Possible Moves: ",allMoves)
printPuzzle(pzl)

