import time

def cross(A, B):
    return [a+b for a in A for b in B]

cols = '123456789'
rows = 'ABCDEFGHI'
digits = cols
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u]) 
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

def createValues(grid):
    values = dict((s, digits) for s in squares)
    for s,d in original_values(grid).items():
        if d in digits and not updateValue(values, s, d):
            return False 
    return values

def original_values(grid):
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    val = dict(zip(squares, chars))
    return val

def updateValue(values, s, d):
    other_values = values[s].replace(d, '')
    if all(removeValues(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def removeValues(values, s, d):
    if d not in values[s]:
        return values 
    values[s] = values[s].replace(d,'')
    if len(values[s]) == 0:
        return False 
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(removeValues(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        for nv in values:
            if len(nv) == 0 or len(nv) == 2:
                len(nv)
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False 
        elif len(dplaces) == 1:
            if not updateValue(values, dplaces[0], d):
                return False
        for nv in values:
            if len(nv) == 0 or len(nv) == 2:
                d3 = nv
    return values

def gameSolver(values):
    if values is False:
        return False 
    if all(len(values[s]) == 1 for s in squares): 
        return values 
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    for d in values[s]:
        BF = gameSolver(updateValue(values.copy(), s, d))
        if BF: return BF
    return False

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
            
            
          
#             
# puzzle = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
#    
# # puzzle = '3.6.7...........518.........1.4.5...7.....6.....2......2.....4.....8.3.....5.....'
# printPuzzle(puzzle)
# values = createValues(puzzle)
# solutions = gameSolver(values)
# line =''
# for key in solutions:
#     line += solutions[key]
# printPuzzle(line)

start_time = time.time()
    
with open("game.txt", "r") as inFile:
    count = 1
    for line in inFile:
        puzzle = line.rstrip()
        print("\n# ", count)
        printPuzzle (puzzle)
        values = createValues(puzzle)
        solutions = gameSolver(values)
        line =''
        count += 1
        if solutions:
            for key in solutions:
                line += solutions[key]
            printPuzzle (line)
        if count > 128:
            break
inFile.close()
 
print("Total Time used: " , time.time() - start_time)
