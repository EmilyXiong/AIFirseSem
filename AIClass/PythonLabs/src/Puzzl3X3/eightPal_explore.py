from tree import Tree
import sys 
import matplotlib.pyplot as plt; plt.rcdefaults()
from numpy.f2py.auxfuncs import ischaracter

puzzle = sys.argv[1]  
firstnode = puzzle.replace('_',' ')
goal=sys.argv[2].replace('_',' ')


movesTree = Tree()
movesTree.add_firstnode(goal)

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

def findSteps(startKey):
    steps=[startKey]
    parent = movesTree.nodes().get(startKey).parentKey()
    while(movesTree.nodes().get(parent).parentKey()  != None):
        parent = movesTree.nodes().get(parent).parentKey() 
        steps.append(parent)
    return steps


def printSteps(steps):
    for step in steps:
        display(step)

def getInversionCount(key):
    invCount = 0
    keywith0 = key.replace(' ','')
    for i in range(0, len(keywith0)-1):
        for j in range(i+1, len(keywith0)):
            if keywith0[i]>keywith0[j]:
                invCount += 1
    return invCount

def isChild(key1, key2):
    if key1 in move(key2):
        return True
    else:
        return False
    
########################################################
if getInversionCount(firstnode) %2 != getInversionCount(goal) %2 :
    print("There is no solution for the input puzzle")
    sys.exit()
    
### builds a complete tree from goal as root.
for node in movesTree.traverse(goal):
    for child in move(node):
        if child not in movesTree.nodes():
            movesTree.add_node(child, node)

print ("Problem 1. The expression for total number of possible stating states is : 9!\n")

maxSteps = movesTree.maxSteps(goal)
print("The hardest puzzle for solving the goal 12345678_ needs = ", maxSteps)       

pzlSteps = findSteps(firstnode)
print("\nProblem 2. The maxSteps between input puzzle ", puzzle, " and the goal is: ", len(pzlSteps))


print ("\nProblem 3. For goal 12345678_, we have 1 to ", maxSteps , " different steps:")
distanceSteps = []
x_pos = []
y_pos = []

for i in range(1, maxSteps+1):
    dist = len(movesTree.nodesAtnthLevel(i))
    distanceSteps.append(dist)
    x_pos.append(i)
    y_pos.append(i-1)
    print(i, ":", dist)
    
allNthNodes = movesTree.nodesAtnthLevel(maxSteps)
print("\nProblem 4. The puzzles take maxSteps ", maxSteps, " to solve are: ")
printSteps(allNthNodes) 
print ("Steps from ", allNthNodes[0].replace(' ', '_'), " to goal ", goal.replace(' ', '_'))
printSteps(findSteps(allNthNodes[0]))
   

plt.bar(y_pos, distanceSteps, align='center', alpha=0.5)
plt.xticks(y_pos, x_pos)
plt.ylabel('Node nubers')
plt.title('Problem 5. Distance to goal')
plt.show()   
    
#for problem 8, we should start from level 31
p_list_list = []
ith_states = movesTree.nodesAtnthLevel(maxSteps)
for N1 in ith_states:
    p_list_list.append([N1])
for i in range(maxSteps-1, 0, -1):
    ith_states = movesTree.nodesAtnthLevel(i)
    for p_list in p_list_list:
        for k1 in ith_states:
            for k2 in p_list:
                if isChild(k1, k2):
                    break
            else:
                p_list.append(k1)
                break
maxstate = 0
print("Problem 8: There are ", len(p_list_list), " largest sets of states. Each set has ", maxSteps, "states that satisfy those two criteria")

for p_list in p_list_list:
    if maxstate < len(p_list):
        maxstate = len(p_list)
for p_list in p_list_list:
    if maxstate == len(p_list):
        print ("\n\n Set contains these states", p_list)
        printSteps(p_list)
        
                    
        

########################################################
    
