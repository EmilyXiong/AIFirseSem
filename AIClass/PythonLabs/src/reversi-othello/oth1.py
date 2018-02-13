import sys

player = 'x'
pzl = "...........................ox......xo..........................."
direction = [-9, -8, -7, -1, 1, 7, 8, 9]
noGo = {-9: [0, 1, 2, 3, 4, 5, 6 ,7 ,8 , 16, 24 ,32, 40, 48, 56], 
        -8: [0, 1, 2, 3, 4, 5, 6, 7],
        -7: [0, 1, 2, 3, 4, 5, 6 , 7, 15, 23, 31, 39, 47, 55, 63],
        -1: [0,8 , 16, 24 ,32, 40, 48, 56],
        1: [7, 15, 23, 31, 39, 47, 55, 63],
        7: [0,8 , 16, 24 ,32, 40, 48, 56, 57, 58, 59, 60, 61, 62, 63],
        8: [56, 57, 58, 59, 60,61, 62, 63],
        9: [7, 15, 23, 31, 39, 47, 55, 56, 57, 58, 59, 60, 61, 62, 63]}

def showBoard(pzl):
    print("")
    for r in range(0,64,8):
        row = str(int(r/8+1)) + ' '
        for ch in pzl[r:r+8]:
            row += ch + " "
        print(row)
    print("  a b c d e f g h" + "\n")

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
        for dir in direction:
            newpos = dir + opp
            if inBoard(newpos) and pzl[newpos]== ".":
                if isLegalMove(pzl, player, newpos, dir):
                    lmoves.add(newpos)
    return lmoves    
            
def isLegalMove(pzl, player, pos, dir):
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

if len(sys.argv) > 2:
    pzl = sys.argv[1].lower()
    player = sys.argv[2].lower()
elif len(sys.argv) == 2:
    pzl = sys.argv[1].lower()
    if pzl.count('.')%2:
        player = 'o'
    else:
        player = 'x'

moves = legalMoves(pzl, player)
for m in moves:
    pzl = pzl[:m] + "*" + pzl[m+1:]
showBoard(pzl)
print("Possible Moves: ", moves)

