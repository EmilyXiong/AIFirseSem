import sys
from select import select
import termios
from sys import stdin

timeout = 150
pzl = '.........'
humanT = 'o'
compT = 'x'
#pzl = "....x...."

winSets = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def showBoard(pzl):
    print(pzl[:3])
    print(pzl[3:6])
    print(pzl[6:], '\n')
    
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

def printStatus(pzl):
    if gameOver(pzl):
        if isWon(pzl, compT):
            print("You Lose!")
        elif isWon(pzl, humanT):
            print("You Win!")
        else:
            print("We Tied!")
        sys.exit()
        
def computerPlay(pzl):
    good, bad, tie = partitionMoves(pzl)
    if good:
        gpos = good.pop()
        pzl = pzl[:gpos] + compT + pzl[gpos+1:]
    elif tie:
        tpos = tie.pop()
        pzl = pzl[:tpos] + compT + pzl[tpos+1:]
    else:
        bpos = bad.pop()
        pzl = pzl[:bpos] + compT + pzl[bpos+1:]
    return pzl

def get_key():
    old = termios.tcgetattr(stdin)
    new = termios.tcgetattr(stdin)
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0
    termios.tcsetattr(stdin, termios.TCSANOW, new)
    key = None
    try:
        key = stdin.read(1)
    finally:
        termios.tcsetattr(stdin, termios.TCSAFLUSH, old)
    return key

def humanPlay(pzl):
#     nextMoves = legalMoves(pzl)
    print("Your turn:   ", end='', flush=True)
    ch =  get_key()
    print(ch)
    pos = int(ch)
    return pzl[:pos] + humanT + pzl[pos+1:]     `

    
if len(sys.argv) > 2:
    pzl = sys.argv[1]
    humanT = sys.argv[2]
    compT = 'o' if humanT=='x' else 'x'
elif len(sys.argv) == 2:
    pzl = sys.argv[1]
    compT, humanT = whosMove(pzl)

newBoard = pzl 
showBoard(pzl)
firstMove, secondMove = whosMove(newBoard)
if firstMove != humanT:
    newBoard = computerPlay(newBoard)
    showBoard(newBoard)
    
while not gameOver(newBoard):    
    newBoard = humanPlay(newBoard)
    showBoard(newBoard)
    if gameOver(newBoard):
        break        
    else:
        newBoard = computerPlay(newBoard)
        showBoard(newBoard)
printStatus(newBoard)

        
