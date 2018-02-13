import sys 

puzzleA = '1234567 8' #sys.argv[1].replace('_',' ')
puzzleB = '84765231 ' #sys.argv[1].replace('_',' ')
puzzleC = '421753 86' #sys.argv[1].replace('_',' ')


def getPosType(puzzle):
    pos = puzzle.find(' ')
    if pos in [0, 2, 6, 8]:
        return 'corner'
    elif pos in [1, 3, 5, 7]:
        return 'egde'
    else:
        return 'center'
    
def rotateCW90(puzzle):
    return puzzle[6]+puzzle[3]+puzzle[0]+puzzle[7]+puzzle[4]+puzzle[1]+puzzle[8]+puzzle[5]+puzzle[2]

def flipH(puzzle):
    return puzzle[2]+puzzle[1]+puzzle[0]+puzzle[5]+puzzle[4]+puzzle[3]+puzzle[8]+puzzle[7]+puzzle[6]

def flipV(puzzle):
    return puzzle[6]+puzzle[7]+puzzle[8]+puzzle[3]+puzzle[4]+puzzle[5]+puzzle[0]+puzzle[1]+puzzle[2]

def applyMap(mapping, puzzle):
    newPuzzle=''
    for ch in puzzle:
        newPuzzle = newPuzzle + mapping[ch]
    return newPuzzle.replace(' ','_')

def getMaaping(p1, p2):
    mapping = {}
    for index in range(0, len(p1)):
        mapping[p1[index]] = p2[index]
    return mapping
        

typeC = getPosType(puzzleC)
typeA = getPosType(puzzleA)
typeB = getPosType(puzzleB)

if typeC != typeA and typeC == typeB:
    tempPzl = puzzleA
    puzzleA = puzzleB
    puzzleB = tempPzl
    tempType = typeA
    typeA = typeB
    typeB = tempType
    
elif typeC != typeA and typeC != typeB:
    print("Type doesn't match, it is very hard to do. Sorry ....")
    sys.exit()
    
#if the type is center no need to rotate or flip
if typeC == 'center':
    mapping = getMaaping(puzzleA, puzzleC)
    print ("The center type can't rotate or flip, the only one solution is:   ", applyMap(mapping, puzzleB))
    sys.exit()


#do the rotation method
puzzleA1 = puzzleA
puzzleB1 = puzzleB
posC = puzzleC.find(' ')
posA = puzzleA1.find(' ')
while posC != posA:
    puzzleA1 = rotateCW90(puzzleA1)
    puzzleB1 = rotateCW90(puzzleB1)
    posA = puzzleA1.find(' ')
    
mapping = getMaaping(puzzleA1, puzzleC)

print ("The first one using rotation method is:   ", applyMap(mapping, puzzleB1))

#do the flip method
puzzleA1 = puzzleA
puzzleB1 = puzzleB
posC = puzzleC.find(' ')
posA = puzzleA1.find(' ')
if posC != posA:
    puzzleA1 = flipV(puzzleA1)
    puzzleB1 = flipV(puzzleB1)
posA = puzzleA1.find(' ')
if posC != posA:
    puzzleA1 = flipV(puzzleA1)
    puzzleB1 = flipV(puzzleB1)
    puzzleA1 = flipH(puzzleA1)
    puzzleB1 = flipH(puzzleB1)
posA = puzzleA1.find(' ')
if posC != posA:
    print ("Can't flip to find the correct position:  exit")
    sys.exit()

mapping = getMaaping(puzzleA1, puzzleC)
print ("The second one using flip method is:   ", applyMap(mapping, puzzleB1))

    
    