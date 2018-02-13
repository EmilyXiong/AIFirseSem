from tree import Tree
import queue as qu
import time
import sys

puzzle = sys.argv[1].replace('_',' ').upper()
#puzzle = ' ONMLKJIHGFEDCBA'    # hang
#puzzle = "AB CEGHDIFLOMKJN"  # should be 14
#puzzle = "ABCDEJ HMOFKNILG"   # should be 19
#puzzle = "AJFCEN DIGBHMOKL"    # should be 17

#firstnode = "64785 321"
goal = "ABCDEFGHIJKLMNO "
             
def display(key):
    print("")
    print (key[:4])
    print (key[4:8])
    print (key[8:12])
    print (key[12:])

def check_goal(key):
    if key == goal:
        return True
    else:
        return False
    
def move(key):
    pos = key.find(' ')
    row = int(pos / 4)
    col = int(pos % 4)
    outlist = []
    if(row > 0):
        outlist.append(swap(key, pos-4, pos ))
    if(row < 3):
        outlist.append(swap(key,pos,pos+4 ))
    if(col > 0):
        outlist.append(swap(key,pos-1,pos ))
    if(col < 3):
        outlist.append(swap(key,pos,pos+1 ))
    return outlist

def swap(s, i, j):
    return ''.join((s[:i], s[j], s[i+1:j], s[i], s[j+1:]))

def findSteps(lastkey, movesTree):
    steps=[lastkey, goal]
    parent = lastkey
    while(movesTree.nodes().get(parent).parentKey()  != None):
        parent = movesTree.nodes().get(parent).parentKey() 
        steps.insert(0, parent)
    return steps

def printSteps(steps):
    for step in steps:
        display(step)
        
def getInversionCount(key):
    invCount = 0
    newkey = key.replace(' ','')
    for i in range(0, len(newkey)-1):
        for j in range(i+1, len(newkey)):
            if ord(newkey[i])>ord(newkey[j]):
                invCount += 1
    return invCount

def isSolveable(key):
    invCount = getInversionCount(key)
    rowCount = key.index(' ') / 4
    if invCount % 2 == rowCount % 2:
        return True
    else:
        return False 

def distanceFromOrigin(currentKey, movesTree):
    steps=0
    parent = movesTree.nodes().get(currentKey).parentKey()
    while(parent != None):
        parent = movesTree.nodes().get(parent).parentKey() 
        steps += 1
    return steps  
            
def manhattan(puzzl):
    key = puzzl.replace(' ', 'P')
    count = 0;
    baseV = ord('A');
    for pos in range(0, 16):
        tile_value = ord(key[pos])-baseV
        if tile_value != pos and tile_value !=15:
            pos_row = int(pos / 4)
            pos_col = int(pos % 4)
            exp_row = int(tile_value / 4)
            exp_col = int(tile_value % 4)
            count += abs(pos_row - exp_row) + abs(pos_col - exp_col)
    return int(count)
  
def game_solver(firstnode, goal): 
    found = False
    allsteps = []
    movesTree = Tree()
    movesTree.add_firstnode(firstnode)

    start_time = time.time()
    
    if isSolveable(firstnode):
        return allsteps, (time.time() - start_time)
    
    totalStates = 0
    loopQueue = qu.PriorityQueue()
    estDis = format(manhattan(firstnode), '02d')
    loopQueue.put(estDis + firstnode)
    closedSet=[]
    openSet=[firstnode]
    while not loopQueue.empty():
        node = loopQueue.get()
        node = node[2:]
        openSet.remove(node)
        closedSet.append(node)
        totalStates += 1
        if found == True:
            break        
        if check_goal(node) == True:
            allsteps = findSteps(node, movesTree)
            found = True
            break
        else:
            costDis1 = distanceFromOrigin(node, movesTree)
            for child in move(node):
                if check_goal(child) == True:
                    allsteps = findSteps(node, movesTree)
                    found = True
                    break
                elif child not in closedSet:
                    estDis2 = manhattan(child)
                    if child not in openSet:
                        movesTree.add_node(child, node)
                        estDis = format(costDis1+estDis2+1, '02d')
                        loopQueue.put(estDis + child)
                        openSet.append(child)
                    
    return allsteps, (time.time() - start_time), totalStates, len(closedSet)


####################################################


solutionSteps, timeUsed, states, closedCount = game_solver(puzzle,goal)

if solutionSteps:
    
    print("The shortest path length is: ", len(solutionSteps)-1)
    print("The number of times an item in openSet was removed: ", states)
    print("THe number of elements in closedSet : ", closedCount)
    print("The time it takes to run is: ", timeUsed)

    #print("Here are the steps for solving the puzzle:")
    #printSteps(solutionSteps)
    
else:
    print("Here is not solution for this game.")
    



##################################################
    

