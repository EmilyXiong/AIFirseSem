import sys
from select import select

pzl = '.........'
humanT = 'o'
compT = 'x'
#pzl = "....x...."

winSets = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def showBoard(pzl):
    print(pzl[:3])
    print(pzl[3:6])
    print(pzl[6:])
    print("\n")
    
def isWon(pzl, player):    
    for s in winSets:
        won = True
        for i in s:
            if pzl[i] != player :
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
    for move in legalMoves(game):
        newGame = game[:move] + player + game[move+1:]
        tmpGood, tmpBad, tmpTie = partitionMoves(newGame)
        if tmpGood:
            bad.add(move)
        elif tmpTie:
            tie.add(move)
        else:
            good.add(move)
    return good, bad, tie       

def legalMoves(pzl):
    return [i for i in range(len(pzl)) if pzl[i] == '.']

def whosMove(pzl):
    if sum(j =='x' for j in pzl) == sum(j =='o' for j in pzl):
        return 'x','o'
    else: 
        return 'o','x'

if len(sys.argv) > 2:
    pzl = sys.argv[1]
    humanT = sys.argv[2]
elif len(sys.argv) == 2:
    pzl = sys.argv[1]
    compT, humanT = whosMove(pzl)

newBoard = pzl 
showBoard(pzl)

while not gameOver(newBoard):    
    good, bad, tie = partitionMoves(newBoard)
    if good:
        gpos = good.pop()
        newBoard = newBoard[:gpos] + compT + newBoard[gpos+1:]
    elif tie:
        tpos = tie.pop()
        newBoard = newBoard[:tpos] + compT + newBoard[tpos+1:]
    else:
        bpos = bad.pop()
        newBoard = newBoard[:bpos] + compT + newBoard[bpos+1:]
    showBoard(newBoard)
    
    if gameOver(newBoard):
        if isWon(newBoard, compT):
            print("You Lose!")
        elif isWon(newBoard, humanT):
            print("You Win!")
        else:
            print("We Tied!")
        break
    
    timeout = 55
    pos = -1
    nextMoves = legalMoves(newBoard)
    
    while(pos == -1):
        print("Please enter your next move. Possible moves: ", nextMoves)
        rlist, wlist, xlist = select([sys.stdin], [], [], timeout)   
        if rlist:        
            pos = int(rlist[0].readline())
            if pos not in nextMoves:
                print("You have entered an invalid move.")
                continue
        else:
            print("Timed out...")

    newBoard = newBoard[:pos] + humanT + newBoard[pos+1:]     
            
    