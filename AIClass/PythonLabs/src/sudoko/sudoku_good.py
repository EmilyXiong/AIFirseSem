import sys
sys.setrecursionlimit(1000000)
b_setlist = [[0,1,2,9,10,11,18,19,20],
          [3,4,5,12,13,14,21,22,23],
          [6,7,8,15,16,17,24,25,26],
          [27,28,29,36,37,38,45,46,47],
          [30,31,32,39,40,41,48,49,50],
          [33,34,35,42,43,44,51,52,53],
          [54,55,56,63,64,65,72,73,74],
          [57,58,59,66,67,68,75,76,77],
          [60,61,62,69,70,71,78,79,80] 
         ]
allValues = set(range(1, 10))
allpositions = list(range(0, 81))
r_setlist = [allpositions[i:i+9] for i in range(0, len(allpositions), 9)] 
c_setlist = [] 
for i in range(0, 9):
    c_setlist.append([j*9+i  for j in range(0, 9)])

all_setlist = list(b_setlist)
all_setlist.extend(r_setlist)
all_setlist.extend(c_setlist)

indexToNbrs = {}
for pos in allpositions:
    templist = []
    for s in all_setlist:
        if pos in s:
            templist.extend(s)
            templist.remove(pos)
    indexToNbrs[pos] = set(templist)
   
def printPuzzle (pzl):
    print ("\n------+------+------")   
    i = 0
    row = 0
    for row in range(0,9):
        col = 0
        line = ''
        for col in range(0, 9):
            line = line + pzl[i] + ' '
            i += 1
            if (col % 3) == 2:
                line = line + '|'
        print (line)
        if (row % 3)==2:
            print ("------+------+------")  

def isSolved(pzl):
    if pzl.find('.') != -1:
        return False
    else:
        return True

def isInvalid(pzl, pos):
    ch = pzl[pos]
    for nbrPos in indexToNbrs[pos]:
        if pzl[nbrPos] == ch:
            return True
    return False
 
def findNextPos(pzl_values):
    minPos = 0
    minNum = 10
    for pos in pzl_values:
        if len(pzl_values[pos]) >1 and len(pzl_values[pos])<minNum:
            minPos = pos
            minNum = len(pzl_values[pos])
    return minPos
        
def createPzlValues(pzl):
    pzl_values = {} 
    for pos in range(0, len(pzl)): 
        if pzl[pos] != '.':
            pzl_values[pos] = set([int(pzl[pos])])
        else:
            ecptValues = set()
            for nbr in indexToNbrs[pos]:
                if pzl[nbr] != '.':
                    ecptValues.add(int(pzl[nbr]))
            pzl_values[pos] = allValues - ecptValues       
    return pzl_values

def isSolvedbyCheck(pzl_values):
#     retPzl = ''
#     for k, v in pzl_values.items():
#         retPzl = retPzl + str(next(iter(pzl_values[k])))
#     printPuzzle(retPzl) 
    for s in all_setlist:
        values=set()
        for index in s:
            values.add(next(iter(pzl_values[index])))
        if len(values) != 9:
            return False
    return True

def gameSolver(pzl):  
    if isSolved(pzl):
        return pzl
    pzl_values = createPzlValues(pzl)
#     for k, v in pzl_values.items():
#         print(k, "---", v)
    if any(len(pzl_values[s]) == 0 for s in pzl_values): 
        return ''
    if all(len(pzl_values[s]) == 1 for s in pzl_values): 
        if isSolvedbyCheck(pzl_values):
            retPzl = ''
            for k, v in pzl_values.items():
                retPzl = retPzl + str(pzl_values[k].pop())
            return retPzl
        return ''
    pos = findNextPos(pzl_values)
    for value in pzl_values[pos]:
        subPzl = pzl[:pos] + pzl[pos:].replace(pzl[pos], str(value), 1)
        if isInvalid(subPzl, pos):
            continue
        else:
            BF = gameSolver(subPzl)
            if BF: return BF
    return ""
    

# pzl = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'   
# pzl = '.2..3..9....9.7...9..2.8..5..48.65..6.7...2.8..31.29..8..6.5..7...3.9....3..2..5.'
# pzl = '...976532.5.123478.3.854169948265317275341896163798245391682754587439621426517983'
# pzl = '..............3.85..1.2.......5.7.....4...1...9.......5......73..2.1........4...9'
# pzl = '....8....27.....54.95...81...98.64...2.4.3.6...69.51...17...62.46.....38....9....'
# # pzl = '3.6.7...........518.........1.4.5...7.....6.....2......2.....4.....8.3.....5.....'
pzl = '1..92....524.1...........7..5...81.2.........4.27...9..6...........3.945....71..6'

printPuzzle (pzl)
# int_pzl_values = createPzlValues(pzl)
# print(int_pzl_values)
solution = gameSolver(pzl)
printPuzzle (solution)

# 
# outFile = open("solvedGames.txt", "w")
#     
# with open("game.txt", "r") as inFile:
#     count = 0
#     for line in inFile:
#         puzzle = line.rstrip()
#         printPuzzle (puzzle)
#         solution = gameSolver(puzzle)
#         count += 1
#         if solution:
#             printPuzzle (solution)
#             outFile.writelines(solution + '\n')
#         else:
#             print ("No soluteion found for this puzzle.")
#             outFile.writelines("No soluteion found for this puzzle.\n")
#         if count > 50:
#             break
# outFile.close()
# inFile.close()

































