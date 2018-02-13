from tree import Tree
import time
import sys 
import queue as qu

puzzle = sys.argv[1].replace('_',' ')
#puzzle = "87 124536"
goal = "12345678 "
ar_pzl = 
mhdList=[[4, 0, 1, 2, 1, 2, 3, 2, 3], [3, 1, 0, 1, 2, 1, 2, 3, 2], [2, 2, 1, 0, 3, 2, 1, 4, 3],
         [3, 1, 2, 3, 0, 1, 2, 1, 2], [2, 2, 1, 2, 1, 0, 1, 2, 1], [1, 3, 2, 1, 2, 1, 0, 3, 2],
         [2, 2, 3, 4, 1, 2, 3, 0, 1], [1, 3, 2, 3, 2, 1, 2, 1, 0], [0, 4, 3, 2, 3, 2, 1, 2, 1]]

def display(key):
    print("")
    print (key[:3])
    print (key[3:6])
    print (key[6:])

def check_goal(key):
    if key == goal:
        return True
    else:
        return False
    
def move(key):
    pos = key.find(' ')
    
    if pos == 0:
        outlist= [swap(key,0,1), swap(key,0,3)]
    elif pos == 1:
        outlist= [swap(key,0,1), swap(key,1,2), swap(key,1,4)]
    elif pos == 2:
        outlist= [swap(key,1,2), swap(key,2,5)]
    elif pos == 3:
        outlist= [swap(key,0,3), swap(key,3,4), swap(key,3,6)]
    elif pos == 4:
        outlist= [swap(key,1,4), swap(key,3,4), swap(key,4,5), swap(key,4,7)]
    elif pos == 5:
        outlist=  [swap(key,2,5), swap(key,4,5), swap(key,5,8)]
    elif pos == 6:
        outlist= [swap(key,3,6), swap(key,6,7)]
    elif pos == 7:
        outlist= [swap(key,4,7), swap(key,6,7), swap(key,7,8)]
    elif pos == 8:
        outlist=  [swap(key,5,8), swap(key,7,8)]

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
            if newkey[i]>newkey[j]:
                invCount += 1
    return invCount

def mhd(key):
    key1 = key.replace(' ', '0')
    mhdCount = 0
    for i in range(0, len(key1)):
        mhdCount += mhdList[i][int(key1[i])]
    return format(mhdCount, '02d')
        

def gamee_solver(firstnode): 
    found = False
    allsteps = []
    movesTree = Tree()
    movesTree.add_firstnode(firstnode)

    start_time = time.time()
    
    if getInversionCount(firstnode) %2 !=  getInversionCount(goal) %2:
        return allsteps, (time.time() - start_time)
    
    loopQueue = qu.PriorityQueue()
    loopQueue.put(mhd(firstnode)+firstnode)
    
    while not loopQueue.empty():
        node = loopQueue.get()
        node = node[2:]
        if found == True:
            break        
        if check_goal(node) == True:
            allsteps = findSteps(node, movesTree)
            found = True
            break
        else:
            for child in move(node):
                if check_goal(child) == True:
                    allsteps = findSteps(node, movesTree)
                    found = True
                    break
                elif child not in movesTree.nodes():
                    movesTree.add_node(child, node)
                    loopQueue.put(mhd(child)+child)
                    
    return allsteps, (time.time() - start_time)

####################################################
if   ''.join(sorted(puzzle)) != ' 12345678':
    print("You have entered an invalid starting state")
    sys.exit()
    
if puzzle == goal:
    print("This is a goal state")
    sys.exit()
    
solutionSteps, timeUsed = gamee_solver(puzzle)
if solutionSteps:
    printSteps(solutionSteps)
    print("There are ", len(solutionSteps)-1, " Steps")
else:
    print("There is no solution")

print(" It took ", timeUsed, " to solve the game")

##################################################
    

