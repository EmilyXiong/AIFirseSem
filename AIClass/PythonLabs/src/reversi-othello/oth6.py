import sys
from _operator import pos

player = 'x'
pzl = "...........................ox......xo..........................."
playPos = -1
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
def inBoard(pos):
    return 0<=pos<=63

def isGoodEdge(pzl, player, pos, di):
    cdir = di
    newpos = pos + cdir
    if pzl[newpos] == player:
        return False
#         while inBoard(newpos):
#             if newpos in noGo[di]:
#                  return pzl[newpos] == player
#             if pzl[newpos] != player:
#                 return False
#             newpos += cdir
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
     
moves = legalMoves(pzl, player)
savedMoves = moves

# Greedy corners: If you can move to a corner, then you should do so
for pos in moves:
    if pos in [i for i in conners if pzl[i]=='.']:
        print(pos)
        sys.exit()

# Safe edges: If you can place a token on an edge such that subsequent to the move from your token to one corner 
# there are only edges with your tokens (no empties or enemy token), then you should do so.
badEdges = set()
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
        print(pos)
        sys.exit()
    if pos in edges_h or pos in edges_v:
        badEdges.add(pos)
moves = moves - badEdges

#You should not play to a C or X square (a square that neighbors a corner) if the corner is not occupied by your own token.
badConners = set()
for pos in conners:
    if pzl[pos] != player:
        moves = moves - conners[pos]
        
if moves:
    print(moves.pop())
elif badEdges:
    print(badEdges.pop())
else:
    print(savedMoves.pop())
    
        

    