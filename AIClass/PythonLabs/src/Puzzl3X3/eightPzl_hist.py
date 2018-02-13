import tree
import sys 
import os
import pickle

def display(key):
    print("")
    print (key[:3])
    print (key[3:6])
    print (key[6:])

def check_goal(key, goal):
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

def findSteps(lastkey, firstkey, goal):
    steps=[lastkey, goal]
    parent = lastkey
    while(movesTree.nodes().get(parent).parentKey()  != None):
        parent = movesTree.nodes().get(parent).parentKey() 
        steps.insert(0, parent)
    return steps

def printSteps(steps):
    for step in steps:
        display(step)

def readHistory(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as pickelFile:
            hisList = pickle.load(pickelFile)
            pickelFile.close()
            return hisList
    else:
        return []
    
def writeHistory(filename, historyDate):
    with open(filename, 'wb') as pickelFile:
        pickle.dump(historyDate, pickelFile, protocol=pickle.HIGHEST_PROTOCOL)
    
firstnode = sys.argv[1].replace('_',' ')   
goal = "12345678 "
if check_goal(firstnode, goal):
    print ("There is a solution with 0 step")
    sys.exit()
    
nonSoluetionMoves = readHistory("nonSoluetionMoves")
if firstnode in nonSoluetionMoves:
    print("There is no solution")
    sys.exit()
 
solutionMoves = readHistory("solutionMoves")   
for his in solutionMoves:
    if firstnode in his:
        allsteps = his[his.index(firstnode):]
        printSteps(allsteps)
        print("There is a solution. There were ", len(allsteps)-1, " steps")
        sys.exit()

movesTree = Tree()
movesTree.add_firstnode(firstnode)
steps = 0
found = False

for node in movesTree.traverse(firstnode):
    if found == True:
        break        
    if check_goal(node, goal) == True:
        allsteps = findSteps(node, firstnode, goal)
        printSteps(allsteps)
        solutionMoves.append(allsteps)
        writeHistory("solutionMoves", solutionMoves)
        found = True
        print("There is a solution. There were ", len(allsteps)-1, " steps")
        break
    else:
        for child in move(node):
            if check_goal(child, check_goal) == True:
                allsteps = findSteps(node, firstnode, goal)
                printSteps(allsteps)
                solutionMoves.append(allsteps)
                writeHistory("solutionMoves", solutionMoves)
                found = True
                print("There is a solution. There were ", len(allsteps)-1, " steps")
                break
            elif child not in movesTree.nodes():
                movesTree.add_node(child, node)
            
else: 
    print("There is no solution")
    nonSoluetionMoves.append(firstnode)
    writeHistory("nonSoluetionMoves", nonSoluetionMoves)
    
    

    