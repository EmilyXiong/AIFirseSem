import sys

#pzl = sys.argv[1]
pzl = "....x...."

winSets = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def showBoard(pzl):
    print ("\n --- --- --- ")   
    for row in range(0,3):
        line = '|'
        for i in range(0, 3):
            line = line + " " + pzl[int(row*3) + i]  + " |" 
        print (line)
        print (" --- --- --- ")  
    
def isWon(pzl, player):
    for s in winSets:
        won = True
        for i in s:
            if pzl[i] != player:
                won = False
                break
        if won:
            return True
    return False

def gameOver(pzl):
    if '.' not in pzl:
        return True
    if isWon(pzl, 'x'):
        return True
    elif isWon(pzl, 'o'):
        return True
    return False

def partitionMoves(game):
    player, opponent = whosMove(game)
    if gameOver(game):
        if isWon(game, player):
            return {''}, set(), set()
        elif isWon(game, opponent):
            return set(), {''}, set()
        else:
            return set(), set(), {''}
    good, bad, tie = set(), set(), set()
    moves = [i for i in range(len(game)) if game[i] == '.']
    for move in moves:
        newGame = game[:move] + player + game[move+1:]
        tmpGood, tmpBad, tmpTie = partitionMoves(newGame)
        if tmpGood:
            bad.add(move)
        elif tmpTie:
            tie.add(move)
        else:
            good.add(move)
    return good, bad, tie       

def whosMove(pzl):
    if sum(j =='x' for j in pzl) == sum(j =='o' for j in pzl):
        return 'x','o'
    else: 
        return 'o','x'

showBoard(pzl)
print(partitionMoves(pzl))
# game = "xxoxo...o"
# print(whosMove(game))
# print(isWon(game, 'o'))