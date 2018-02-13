
pzl = '....X....'
nbrs = [[0, 1, 2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def printPuzzle (pzl):
    print ("\n+___+___+___+")   
    for row in range(0,3):
        line = '|'
        for i in range(0, 3):
            line = line + " " + pzl[int(row*3) + i]  + " |" 
        print (line)
        print ("+___+___+___+")  
            
def nextMove(pzl):
    if sum(j=='X' for j in pzl) <= sum(j=='O' for j in pzl):
        return 'X'
    else:
        return 'O'
    
def emptyPositions(pzl):
    return {i for i in range(len(pzl)) if pzl[i]=='.'}

ML = nextMove(pzl)
if ML == 'X':
    OL = 'O'
else:
    OL = 'X'


def won(game, lable):
    for s in nbrs:
        hasWon = True
        for pos in s:
            if game[pos] != lable:
                hasWon = False
                break;
        if hasWon:
            return True
    return False


def partitionMoves(game): #return 3 sets of moves- good, bad, neutral
    if won(game, OL):
        return ({''}, {},{})
    if won(game, ML):
        return ({},{''},{})
    else:  
        return ({},{},{''})
    good, bad, tie = set(), set(), set()
    for move in emptyPositions(game): 
        newGame = game[:move] + nextMove(game) +  game[move+1:]   #'newGame.replace('.', nextMove(game), 1)
        printPuzzle(newGame)
        tmpGood, tmpBad, tmpTie = partitionMoves(newGame)
        if tmpGood: 
            bad.add(move) #if good for oppenent bad for us
        elif tmpTie: 
            tie.add(move)
        else: 
            good.add(move)
    return good, bad, tie

printPuzzle(pzl)

 
print( whoMove(pzl))
print(emptyPosition(pzl))
good, bad, tie = partitionMoves(pzl)
print("good set:", good)
print("bad set:", bad)
print("tie set:", tie)
