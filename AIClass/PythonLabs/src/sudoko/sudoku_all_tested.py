import time

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
allValues = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
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
            
def findNextPos(pzl_values):
    minPos = 0
    minNum = 10
    for pos in pzl_values:
        size = len(pzl_values[pos])
        if size >1 and size < minNum:
            minPos = pos
            minNum = size
    return minPos
        
def createPzlValues(pzl):
    pzl_values = {} 
    for pos in range(0, len(pzl)): 
        if pzl[pos] != '.':
            pzl_values[pos] = pzl[pos]
        else:
            ecptValues = set()
            for nbr in indexToNbrs[pos]:
                if pzl[nbr] != '.':
                    ecptValues.add(pzl[nbr])
            pzl_values[pos] = ''.join(allValues - ecptValues)   
    return pzl_values

def isInvalid(pzl_values, prePos):
    if any(len(pzl_values[s]) == 0 for s in pzl_values): 
        return True    
    return False
 
def isSolved(pzl_values):
    if all(len(pzl_values[pos]) == 1 for pos in pzl_values): 
        return True
    return False

def createNewValues(newValues, pos, value):
    newValues[pos] = value
    for nbr in indexToNbrs[pos]:
        plen = len(newValues[nbr])
        newValues[nbr] = newValues[nbr].replace(value, '')
        alen = len(newValues[nbr])
        # If a pos s is reduced to one value then that value need to be reduced from the peers.
        if plen == 2 and alen == 1:
            newValues = createNewValues(newValues, nbr, newValues[nbr])
    for s in all_setlist:
        if pos in s:
            remainValues = '123456789'
            for index in s:
                if len(newValues[index]) == 1:
                    remainValues = remainValues.replace(newValues[index], '')
            for v in remainValues:
                dplaces = [index for index in s if v in newValues[index]]
                if len(dplaces) == 1:
                    newValues = createNewValues(newValues, dplaces[0], v)
                    
    return newValues
                       
def gameSolver(pzl_values, prePos):  
    if isInvalid(pzl_values, prePos):  return False
    if isSolved(pzl_values):  return pzl_values
    pos = findNextPos(pzl_values)
    for value in pzl_values[pos]:
        newValues = createNewValues(pzl_values.copy(), pos, value)
        BF = gameSolver(newValues, pos)
        if BF: return BF
    return False


    
    
# pzl = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'   
# pzl = '.2..3..9....9.7...9..2.8..5..48.65..6.7...2.8..31.29..8..6.5..7...3.9....3..2..5.'
# pzl = '...976532.5.123478.3.854169948265317275341896163798245391682754587439621426517983'
# pzl = '..............3.85..1.2.......5.7.....4...1...9.......5......73..2.1........4...9'
# pzl = '....8....27.....54.95...81...98.64...2.4.3.6...69.51...17...62.46.....38....9....'
# pzl = '3.6.7...........518.........1.4.5...7.....6.....2......2.....4.....8.3.....5.....'
# pzl = '...6.2...4...5...1.85.1.62..382.671...........194.735..26.4.53.9...2...7...8.9...'
# pzl = '1..92....524.1...........7..5...81.2.........4.27...9..6...........3.945....71..6'
pzl = '..............3.85..1.2.......5.7.....4...1...9.......5......73..2.1........4...9'


printPuzzle (pzl)
int_pzl_values = createPzlValues(pzl)
# print(int_pzl_values)
solution = gameSolver(int_pzl_values, 0)
if solution:
    retPzl = ''
    for k, v in solution.items():
        retPzl = retPzl + v
    printPuzzle (retPzl)
else:
    print ("No soluteion found for this puzzle.")

start_time = time.time()
with open("game.txt", "r") as inFile:
    count = 1
    for line in inFile:
        puzzle = line.rstrip()
        print("\n# ", count)
        printPuzzle (puzzle)
        int_pzl_values = createPzlValues(puzzle)
        solution = gameSolver(int_pzl_values, 0)
        count += 1
        printPuzzle (solution)
#         if count > 129:
#             break
inFile.close()
 
 
 
 
print("Total Time used: " , time.time() - start_time)





























