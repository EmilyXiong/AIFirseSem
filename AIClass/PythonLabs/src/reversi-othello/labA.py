import sys
import random

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

def showBoard(pzl):
    for r in range(0,64,8):
        row = ''
        #row = str(r//8 + 1) + ' '
        for ch in pzl[r:r+8]:
            row += ch + " "
        print(row)
    #print("  a b c d e f g h")

def getOpp(player):
    if player == "x":
        return "o"
    else:
        return "x"

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

def isValidBoardArgument(inArgument):
    if len(inArgument) != 64:
        return False
    else:
        for ch in inArgument:
            if ch not in ['o', 'O', 'x', 'X', '.']:
                return False
    return True

def isValidPosArgument(inArgument):
    if not inArgument.isdigit() or int(inArgument) < 0 or int(inArgument) > 63:
        return False
    return True

def isValidPlayerArgument(inArgument):
    if inArgument not in ['o', 'O', 'x', 'X']:
        return False
    return True

def converPosition(inArgument):
    if not inArgument.isdigit():
        if len(inArgument) ==2:
            return int(ord(inArgument[0].lower()) - 97 + (int(inArgument[1])-1)*8)
        else:
            return -1
    return int(inArgument)

def exitGameWithError(errorMsg):
    print(errorMsg)
    sys.exit()
    
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

playertable = {'o': 'x', 'x':'o'}

def makeMove(pzl, player, pos):
    newPzl = pzl
    for dire in direction:
        flipPos = pos - dire
        if isLegalMove(pzl, player, pos, dire):
            while pzl[flipPos] != player:
                newPzl = newPzl[:flipPos] + player + newPzl[flipPos+1:]
                flipPos = flipPos - dire
    newPzl = newPzl[:pos] + player + newPzl[pos+1:]
             
    return newPzl

def bestMoves(pzl, player):
    corners = set()
    safeEdges = set()
    badNeighbors = set()
    badEdges = set()
    moves = legalMoves(pzl, player)
    savedMoves = moves
    
    for pos in moves:
        if pos in [i for i in conners if pzl[i]=='.']:
            corners.add(pos)
    if corners: return corners
    
    for pos in moves:
        isSafeEdge = False
        if pos in edges_h:
            for d in [-1, 1]:
                isSafeEdge = isGoodEdge(pzl, player, pos, d)
                if isSafeEdge: break
        elif pos in edges_v:
            for d in [-8, 8]:
                isSafeEdge = isGoodEdge(pzl, player, pos, d)
                if isSafeEdge: break
        if isSafeEdge:
            safeEdges.add(pos)
        if pos in edges_h or pos in edges_v:
            badEdges.add(pos)
    if safeEdges: return safeEdges
    moves = moves - badEdges
    
    for pos in conners:
        if pzl[pos] != player:
            badNeighbors.update(conners[pos])
            
    inners = moves - badNeighbors
    if inners:
        return inners
    elif badEdges:
        return badEdges
    else:
        return savedMoves

def evalBoard(pzl, token):
    return pzl.count(token) - (pzl.count(playertable[token]))

def negamax(board, token, levels, still_running):  
    if still_running == 0:
        sys.exit()
    lm = bestMoves(board, token)
    if len(lm)== 0 and len(legalMoves(board, playertable[token])) == 0: 
        return [evalBoard(board, token)]
    #lm = legalMoves(board, token)
    if not lm:
        nm = negamax(board, playertable[token], levels-1, still_running) + [-1]
        #miniscores.insert(0, nm)
        return [-nm[0]] + nm[1:]
    nmList = sorted([negamax(makeMove(board, token, move), playertable[token], levels-1, still_running) + [move] for move in lm])    
    best = nmList[0]
    return [-best[0]] + best[1:]

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

# else:
#     showBoard(pzl) 
#     print(legalMoves(pzl, player))
#     sys.exit()
EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
class Strategy():
    def best_strategy(self, board, player, best_move, still_running):
        brd = ''.join(board).replace('?','').replace('@','x')
        token = 'x' if player == '@' else 'o'
        if board.count('.') <=8:
            mv = negamax(brd, token, -1, still_running.value)
            mv1 = 11 + (mv[-1]//8)*10 + (mv[-1]%8)
            best_move.value = mv1
        else:
            mv = random.choice([*bestMoves(pzl,player)])
            mv1 = 11 + (mv[-1]//8)*10 + (mv[-1]%8)
            best_move.value = mv1


def main():
    showBoard(pzl)   
    moves = legalMoves(pzl, player)
    print(moves)
    
    if pzl.count('.')<=8:    
        nm = negamax(pzl, player, -1) #1, 3, 5, 7, 9   
        print('At level {} nm gives {} and I pick heuristic move {}'.format(-1, nm, nm[-1]))
    else:
        print(random.choice([*bestMoves(pzl,player)]))
if __name__ == "__main__":
    main()