set3x3 = [[0,1,2,9,10,11,18,19,20],
          [3,4,5,12,13,14,21,22,23],
          [6,7,8,15,16,17,24,25,26],
          [27,28,29,36,37,38,45,46,47],
          [30,31,32,39,40,41,48,49,50],
          [33,34,35,42,43,44,51,52,53],
          [54,55,56,63,64,65,72,73,74],
          [57,58,59,66,67,68,75,76,77],
          [60,61,62,69,70,71,78,79,80] 
         ]

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
            
def isInvalid(pzl, pos, value):
    
    #check if the value at pos is valid for 3x3 square
    for s in set3x3:
        if pos in s:
            for set_pos in s:
                if pzl[set_pos] == value:
                    return True
            break  # pos only benlongs to one 3x3 set
    
    #check if the value at pos is valid for the current row
    crrent_row = int(pos / 9)
    for i in range (0, 9):
        if pzl[crrent_row*9 +i] == value:
            return True
        
    #check if the value at pos is valid for the current column
    corrent_col = pos % 9
    for j in range(0, 9):
        if pzl[j*9 + corrent_col] == value:
            return True
    # passed all three tests. this is a valid value at this pos
    return False

def isSolved(pzl):
    if pzl.find('.') != -1:
        return False
    else:
        return True
    
def gameSolver(pzl): 
    if isSolved(pzl):
        return pzl
    pos = pzl.find('.')
    for i in range(1, 10):
        subPul = pzl
        if isInvalid(subPul, pos, str(i)):
            continue
        else:
            subPzl = subPul.replace('.', str(i), 1)
            bF = gameSolver(subPzl)
            if bF:  return bF
    return ""
            
 
 
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
#         if count > 51:
#             break
# outFile.close()
# inFile.close()

        
        
# puzzle = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
# puzzle = '1..92....524.1...........7..5...81.2.........4.27...9..6...........3.945....71..6'
# puzzle = '3.6.7...........518.........1.4.5...7.....6.....2......2.....4.....8.3.....5.....'
puzzle = '..............3.85..1.2.......5.7.....4...1...9.......5......73..2.1........4...9'

printPuzzle (puzzle)
solution = gameSolver(puzzle)
if solution:
    printPuzzle (solution)
else:
    print ("No soluteion found for this puzzle.")
 
                     
         
    
    