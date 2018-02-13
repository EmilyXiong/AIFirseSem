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

#nt_pzl_values = dict((pos, values) for pos in allpositions)    
   

  
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

def isSolved(pzl_values):
    if all(len(pzl_values[s]) == 1 for s in pzl_values): 
        return True 
    else:
        return False

def isValid(pzl_values, pos, value):
    new_pzl_values = pzl_values.copy()
    new_pzl_values[pos] = set([value])
    allItems = []
    for nbr in indexToNbrs[pos]:
        new_pzl_values[nbr].discard(value)
        if  not new_pzl_values[nbr]:
                return {}
        elif new_pzl_values[nbr] in allItems:
            return {}
        else:
            allItems.append(new_pzl_values[nbr])
            
    return new_pzl_values

def findNextPos(pzl_values):
    minPos = 0
    minNum = 10
    for pos in pzl_values:
        if len(pzl_values[pos]) >1 and len(pzl_values[pos])<minNum:
            minPos = pos
            minNum = len(pzl_values[pos])
    return minPos
        

def gameSolver(pzl_values):  
    if isSolved(pzl_values):
        return pzl_values
    pos = findNextPos(pzl_values)
    for value in pzl_values[pos]:
        new_pzl_values = isValid(pzl_values, pos, value)
        if not new_pzl_values:
            continue
        else:
            BF = gameSolver(new_pzl_values)
            if BF: return BF
    return {}
    

pzl = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'   

int_pzl_values = createPzlValues(pzl)
print(int_pzl_values)
solution = gameSolver(int_pzl_values)
print (gameSolver(solution))

