import sys
import math

direction = [-9, -8, -7, -1, 1, 7, 8, 9]
noGo = {-9: [0, 1, 2, 3, 4, 5, 6 ,7 ,8 , 16, 24 ,32, 40, 48, 56], 
        -8: [0, 1, 2, 3, 4, 5, 6, 7],
        -7: [0, 1, 2, 3, 4, 5, 6 , 7, 15, 23, 31, 39, 47, 55, 63],
        -1: [0,8 , 16, 24 ,32, 40, 48, 56],
        1: [7, 15, 23, 31, 39, 47, 55, 63],
        7: [0,8 , 16, 24 ,32, 40, 48, 56, 57, 58, 59, 60, 61, 62, 63],
        8: [56, 57, 58, 59, 60,61, 62, 63],
        9: [7, 15, 23, 31, 39, 47, 55, 56, 57, 58, 59, 60, 61, 62, 63]}
conners = {0:{1,8,9}, 7:{6,14,15}, 56:{48,49,57}, 63:{54,55,62}}
edges_h = [1,2,3,4,5,6,57,58,59,60,61,62]
edges_v = [8,16,24,32,40,48,15,23,31,39,47,55]
INFINITE = math.inf
DEPTH = 10

def getOpp(player):
    if player == "x": return "o"
    else: return "x"

def findOpp(pzl, player):
    opp = getOpp(player)
    olist = []
    for pos in range(len(pzl)):
        if pzl[pos] == opp:
            olist.append(pos)
    return olist
    
def legalMoves(pzl, player):
    olist = findOpp(pzl, player)
    lmoves = set()
    for opp in olist:
        for di in direction:
            newpos = di + opp
            if inBoard(newpos) and pzl[newpos]== ".":
                if isLegalMove(pzl, player, newpos, di):
                    lmoves.add(newpos)
    return lmoves            
             
def isLegalMove(pzl, player, pos, di):
    cdir = 0 - di
    newpos = pos + cdir
    while inBoard(newpos):
        if newpos in noGo[di]:
            return False
        if pzl[newpos] == ".":
            return False
        elif pzl[newpos] == player:
            return True
        else:
            newpos += cdir
def flip(pzl, player, pos):
    newPzl = pzl
    for dir in direction:
        flipPos = pos - dir
        if isLegalMove(pzl, player, pos, dir):
             while pzl[flipPos] != player:
                newPzl = newPzl[:flipPos] + player + newPzl[flipPos+1:]
                flipPos = flipPos - dir
    newPzl = newPzl[:pos] + player + newPzl[pos+1:]
             
    return newPzl

def needFlip(pzl, player, pos, dir):
    cdir = 0 - dir
    newpos = pos + cdir
    while inBoard(newpos):
        if newpos in noGo[dir]:
            return False
        if pzl[newpos] == ".":
            return False
        elif pzl[newpos] == player:
            return True
        else:
            newpos += cdir
            
            
def inBoard(pos):
    return 0<=pos<=63

def CountScore(pzl, player, pos):
    newPzl = pzl
    for dir in direction:
        flipPos = pos - dir
        if isLegalMove(pzl, player, pos, dir):
             while pzl[flipPos] != player:
                newPzl = newPzl[:flipPos] + player + newPzl[flipPos+1:]
                flipPos = flipPos - dir
    newPzl = newPzl[:pos] + player + newPzl[pos+1:]
             
    return newPzl.count(player)

def needFlip(pzl, player, pos, dir):
    cdir = 0 - dir
    newpos = pos + cdir
    while inBoard(newpos):
        if newpos in noGo[dir]:
            return False
        if pzl[newpos] == ".":
            return False
        elif pzl[newpos] == player:
            return True
        else:
            newpos += cdir
            
def isGoodEdge(pzl, player, pos, di):
    cdir = di
    newpos = pos + cdir
    if pzl[newpos] == player:
        while inBoard(newpos):
            if newpos in noGo[di]:
                 return pzl[newpos] == player
            if pzl[newpos] != player:
                return False
            newpos += cdir
    else:
        oppoToken = getOpp(player)
        canflip = True
        while inBoard(newpos):
            if newpos in noGo[di]:
                 return pzl[newpos] == player
            if pzl[newpos] == '.':
                return False
            if pzl[newpos] == oppoToken and not canflip:
                return False
            elif pzl[newpos] == player and canflip:
                canflip = False
            else:
                newpos += cdir

def bestMoves(pzl, player):
    corners = set()
    safeEdges = set()
    inners = set()
    badNeibrs = set()
    badEdges = set()
    
    moves = legalMoves(pzl, player)
    savedMoves = moves

    # Greedy corners: If you can move to a corner, then you should do so
    for pos in moves:
        if pos in [i for i in conners if pzl[i]=='.']:
            corners.add(pos)
    if corners: return corners
    
    # Safe edges: If you can place a token on an edge such that subsequent to the move from your token to one corner 
    # there are only edges with your tokens (no empties or enemy token), then you should do so.
    for pos in moves:
        isSaftEdge = False
        if pos in edges_h:
            for d in [-1, 1]:
                isSaftEdge = isGoodEdge(pzl, player, pos, d)
                if isSaftEdge: break            
        elif pos in edges_v:
            for d in [-8, 8]:
                isSaftEdge =  isGoodEdge(pzl, player, pos, d)
                if isSaftEdge: break
        if isSaftEdge:
            safeEdges.add(pos)
        if pos in edges_h or pos in edges_v:
            badEdges.add(pos)
    if safeEdges: return safeEdges
    moves = moves - badEdges
    
    #You should not play to a C or X square (a square that neighbors a corner) if the corner is not occupied by your own token.
    badConners = set()
    for pos in conners:
        if pzl[pos] != player:
            badNeibrs.update(conners[pos])
    
    inners  = moves - badNeibrs
    if inners:
        return inners
    elif badEdges:
        return badEdges
    else:
        return savedMoves

def minimax(pzl, depth, player, isMaxPlayer):
    if depth == DEPTH or pzl.count('.') == 0:
        return pzl.count(player) 
    if isMaxPlayer :
        bestVal = - INFINITE
        nextMoves = bestMoves(pzl, player)
        if not nextMoves:  
            newPzl = pzl
            bestVal = minimax(newPzl, depth+1, player, False)
        for pos in nextMoves :
            newPzl = flip(pzl, player, pos)
            value = minimax(newPzl, depth+1, player, False)
            bestVal = max( bestVal, value) 
        return bestVal
    else :
        bestVal = INFINITE 
        nextMoves = bestMoves(pzl, getOpp(player))
        if not nextMoves:
            newPzl = pzl
            bestVal =  minimax(newPzl, depth+1,player, True)
        for pos in nextMoves :
            newPzl = flip(pzl, getOpp(player), pos)
            value = minimax(newPzl, depth+1,player, True)
            bestVal = min( bestVal, value) 
        return bestVal
    
def findBestMove(pzl, player):
    bestValue = -INFINITE
    nextMoves = bestMoves(pzl, player)
    bestMove = nextMoves.pop()
    print(bestMove)
    for pos in nextMoves :
        newPzl = flip(pzl, player, pos)
        value = minimax(newPzl, 0, player, False)
        if value > bestValue:
            bestValue = value
            bestMove = pos
    return bestMove

if len(sys.argv) == 3:
    pzl = sys.argv[1].lower()
    player = sys.argv[2].lower()
elif len(sys.argv) == 2:
    if len(sys.argv[1]) == 64:
        pzl = sys.argv[1].lower()
        if pzl.count('.')%2:
            player = 'o'
        else:
            player = 'x'
    else:
        player = sys.argv[1].lower()
else:
    print(pzl + " "+ str(pzl.count('x')) + '/'+ str(pzl.count('o')))
    sys.exit()
      
     
# player = 'x'
# pzl = "...........................OX......XO...........................".lower()

nextMove = findBestMove(pzl, player)
print(nextMove)
    