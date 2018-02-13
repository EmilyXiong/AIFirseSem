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
    print("")
    for r in range(0,64,8):
        row = str(int(r/8+1)) + ' '
        for ch in pzl[r:r+8]:
            row += ch + " "
        print(row)
    print("  a b c d e f g h")

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
    
def flip(pzl, player, pos):
    newPzl = pzl
    for di in direction:
        flipPos = pos - di
        if isLegalMove(pzl, player, pos, di):
             while pzl[flipPos] != player:
                 newPzl = newPzl[:flipPos] + player + newPzl[flipPos+1:]
                 flipPos = flipPos - di
    newPzl = newPzl[:pos] + player + newPzl[pos+1:]
             
    return newPzl

def needFlip(pzl, player, pos, di):
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

def isValidPosArgument(inArgument):
    if not inArgument.isdigit() or int(inArgument) < 0 or int(inArgument) > 63:
        return False
    return True

def isValidBoardArgument(inArgument):
    if len(inArgument) != 64:
        return False
    else:
        for ch in inArgument:
            if ch not in ['o', 'O', 'x', 'X', '.']:
                 return False
    return True

def isValidPlayerArgument(inArgument):
    if inArgument not in ['o', 'O', 'x', 'X']:
        return False
    return True

def exitGameWithError(errorMsg):
    print(errorMsg)
    sys.exit()

## parsing input arguments
if len(sys.argv) == 4:
    if isValidBoardArgument(sys.argv[1]) and isValidPlayerArgument(sys.argv[2]) and isValidPosArgument(sys.argv[3]):
        pzl = sys.argv[1].lower()
        player = sys.argv[2].lower()
        playPos = int(sys.argv[3])
    else:
        exitGameWithError("Invalid argument(s) !")
elif len(sys.argv) == 3: #only two arguments either board, pos or player, pos
    if not isValidPosArgument(sys.argv[2]):
        exitGameWithError("Invalid position argument !")
    playPos = int(sys.argv[2])
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
elif len(sys.argv) == 2: # only one argument and it must be pos
    if not isValidPosArgument(sys.argv[1]):
        exitGameWithError("Invalid position argument !")
    playPos = int(sys.argv[1])
else:
    exitGameWithError("Invalid argument numbers !")

moves = legalMoves(pzl, player)
print("Game = '" + pzl + "'  player='" + player + "'  position= ", playPos)
print("Possible Moves: ", moves)

if playPos not in moves:
    exitGameWithError("Invalid move.")

newPzl = flip(pzl, player, playPos)
showBoard(newPzl)
print(newPzl+ "   "+ str(newPzl.count('x')) +  '/'+ str(newPzl.count('o'))+"\n")



