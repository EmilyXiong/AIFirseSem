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

def converPosition(inArgument):
    if not inArgument.isdigit():
        if len(inArgument) ==2:
            return int(ord(inArgument[0]) - 97 + (int(inArgument[1])-1)*8)
        else:
            return -1
    return int(inArgument)

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
    
startPosIndex = 0
maxArgumentIndex = len(sys.argv) -1
if maxArgumentIndex == 0:
    showBoard(pzl)
    print(pzl+ " "+ str(pzl.count('x')) +  '/'+ str(pzl.count('o')))
    sys.exit()
in1 = sys.argv[1].lower()
if isValidBoardArgument(in1):
    pzl = in1
    if isValidPlayerArgument(sys.argv[2]):
        player = sys.argv[2].lower()
        startPosIndex = 3
    else:
        if pzl.count('.')%2:
            player = 'o'
        else:
            player = 'x'
        startPosIndex= 2
elif isValidPlayerArgument(sys.argv[1]):
    player = in1
    startPosIndex = 2
else:
    startPosIndex = 1

currentIndex = startPosIndex
newPzl = pzl
# showBoard(pzl)
# print("Game = '" + pzl + "'  player='" + player + "'  position= ", sys.argv[currentIndex])


while currentIndex <= maxArgumentIndex:
    moves = legalMoves(newPzl, player)
    if moves: 
        playPos = converPosition(sys.argv[currentIndex].lower())
        #print("Game = '" + newPzl + "'  player='" + player + "'  position= ", playPos)
        if not inBoard(playPos) or playPos not in moves:
            exitGameWithError("A invalid move detected.     " + sys.argv[currentIndex])
       
        #showBoard(newPzl)
        newPzl = flip(newPzl, player, playPos)
        #showBoard(newPzl)

        currentIndex +=1
        player = getOpp(player)
    else: #force pass
        player = getOpp(player)
   
showBoard(newPzl)
print(newPzl+ " "+ str(newPzl.count('x')) +  '/'+ str(newPzl.count('o')))

