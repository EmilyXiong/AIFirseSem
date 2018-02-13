from tree import Tree
import sys 
import matplotlib.pyplot as plt; plt.rcdefaults()
from numpy.f2py.auxfuncs import ischaracter
from matplotlib.pyplot import step

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

def displayAll(steps, n_perRow):
    print("\n")
    lastRowCount = int(len(steps) % n_perRow)
    full_rows = int(len(steps) / n_perRow)
    for i in range(0, full_rows):
        row1=''
        row2=''
        row3=''
        for j in range(0, n_perRow):
            k = int(i*n_perRow)
            row1 = row1 + steps[k+j][:3] + "   "
            row2 = row2 + steps[k+j][3:6] + "   "
            row3 = row3 + steps[k+j][6:] + "   "
        print(row1)
        print(row2)
        print(row3)
        print("\n")
    row1=''
    row2=''
    row3=''
    for j in range(0, lastRowCount):
        k = int(full_rows*n_perRow)
        row1 = row1 + steps[k+j][:3] + "   "
        row2 = row2 + steps[k+j][3:6] + "   "
        row3 = row3 + steps[k+j][6:] + "   "
    print(row1)
    print(row2)
    print(row3)
    print("\n")

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


print ("\nProblem 3. For goal ", goal, " we have 1 to ", maxSteps , " different steps:")
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
#printSteps(allNthNodes) 
displayAll(allNthNodes, 8)
print ("Steps from ", allNthNodes[0].replace(' ', '_'), " to goal ", goal.replace(' ', '_'))
#printSteps(findSteps(allNthNodes[0]))
displayAll(findSteps(allNthNodes[0]), 8)
   

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
for i in range(maxSteps-1, 0, -1):  #for each level of the whole tree
    ith_states = movesTree.nodesAtnthLevel(i) #get all the nodes at the level
    for p_list in p_list_list: 
        for k1 in ith_states:    # make sure the node we pick from this level k1 is not child of those nodes in formed sets
            for k2 in p_list:
                if isChild(k1, k2):   
                    break      #No state in 𝑆 should be a distance of 1 from any other state in 𝑆.
            else:
                p_list.append(k1)
                break
maxstate = 0
print("Problem 8: There are ", len(p_list_list), " largest sets of states. Each set has ", len(p_list_list[0]), "states that satisfy those TWO criteria")

for p_list in p_list_list:
    if maxstate < len(p_list):
        maxstate = len(p_list)
for p_list in p_list_list:
    if maxstate == len(p_list):
        print ("\n\n Set contains these states are: ")
        #printSteps(p_list)
        displayAll(p_list, 8)
                    
        
#for problem 8a, we should start from level 31
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
                goal_path = findSteps(k2)  # For each state in 𝑆, there is a shortest path to the goal
                if k1 in goal_path:
                    break
            else:
                p_list.append(k1)
                break
maxstate = 0
print("Problem 8a: There are ", len(p_list_list), " largest sets of states. Each set has ", len(p_list_list[0]), "states that satisfy those THREE criteria")

for p_list in p_list_list:
    if maxstate < len(p_list):
        maxstate = len(p_list)
for p_list in p_list_list:
    if maxstate == len(p_list):
        print ("\n\n Set contains these states are: ")
        #printSteps(p_list)
        displayAll(p_list, 8)
########################################################
    
