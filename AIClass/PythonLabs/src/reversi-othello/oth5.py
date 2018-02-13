import sys

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

def isValidPosArgument(inArclgument):
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

if len(sys.argv) == 3:
    if isValidBoardArgument(sys.argv[1]) and isValidPlayerArgument(sys.argv[2]):
        pzl = sys.argv[1].lower()
        player = sys.argv[2].lower()
    else:
        exitGameWithError("Invalid argument(s) !")
elif len(sys.argv) == 2:
    if isValidBoardArgument(sys.argv[1]):
        pzl = sys.argv[1].lower()
        if pzl.count('.')%2:
            player = 'o'
        else:
            player = 'x'
    elif isValidPlayerArgument(sys.argv[1]):
        player = sys.argv[1].lower()
    else:
        exitGameWithError("Invalid board or player argument !")
else:
    showBoard(pzl)
    print(pzl + " "+ str(pzl.count('x')) + '/'+ str(pzl.count('o')))
    sys.exit()
    
moves = legalMoves(pzl, player)
# print(moves)
if moves:
    print(moves.pop())

    