from vertice import vertice
from distanceDemo import calcdv
from nodeEdge import nodeEdge
import matplotlib.pyplot as plt
import sys
import time

startName = sys.argv[1]
goalName = sys.argv[2]

x_values =[]
y_values = []
railroadNet = {}
nodeNames=[]
cityNameMap ={}

#read in romNodes.txt to build the graph with vertices
def readNodes(fileName):
    with open(fileName, "r") as nodeFile:
        for line in nodeFile:
            line = line.rstrip().split(" ")
            #create a vertice
            x = float(line[1])
            y = float(line[2])
            v = vertice(line[0], x, y)  
            x_values.append(x)
            y_values.append(y)
            #add vertice to graph
            railroadNet[line[0]] = v
            nodeNames.append(line[0])

def readFullName(fileName):        
    #Now open file romFullName.txt to add the full names to vertices
    with open(fileName, "r") as fullNameFile:
        index = 0
        for line in fullNameFile:
            cityName = line.rstrip()
            v = railroadNet[nodeNames[index]]
            v.setFullName(cityName)
            cityNameMap[cityName] = v.getName()
            index += 1
  
def readNodeCity(fileName):
    #Open rrNodeCity.txt to to add the full names to vertices
    with open(fileName, "r") as cityFile:
        for line in cityFile:
            line = line.rstrip()
            cityId = line[:7]
            city = line[8:]
            v = railroadNet[cityId]
            v.setFullName(city)
            cityNameMap[city] = cityId
    
def readEdges(fileName):      
    #Open romEdges.txt to build edges for each vertice
    with open(fileName, "r") as edgesFile:
        for line in edgesFile:
            vs = line.rstrip().split(' ')
            v0 = railroadNet[vs[0]]
            v1 = railroadNet[vs[1]]
            d = calcdv(v0, v1)
            newEdge = nodeEdge(vs[0],vs[1], d)
            v0.addEdge(newEdge)
            v1.addEdge(newEdge)

def resetEdgeMark():
    for name in nodeNames:
        v = railroadNet[name]
        for edge in v.getEdges():
            edge.setVisited(False)
                
def displayDistance():
    #calculate sum of all edge's distances 
    sumDistance = 0.0
    for name in nodeNames:
        v = railroadNet[name]
        for edge in v.getEdges():
            if not edge.hasVisited():
                edge.setVisited(True)
                sumDistance += edge.getDistance()
                print("edge between " + edge.getFromNodeName() + " and " + edge.getToNodeName() + " is: ", edge.getDistance())
    resetEdgeMark()
    print("Sum of all edges are:", round(sumDistance,1))

def drawGraph(fig, ax):
    #draw graph 
    for name in nodeNames:
        v = railroadNet[name]
        #class matplotlib.pyplot.Circle(xy, radius=5, **kwargs)
        circle = plt.Circle( (v.getY(),v.getX()),  0.2, facecolor='y', edgecolor='b')
        ax.add_artist(circle)
        plt.text(v.getY()-0.1, v.getX(),v.getName())
        for edge in v.getEdges():
            if not edge.hasVisited():
                edge.setVisited(True)
                ev = railroadNet[edge.getToNodeName()]
                plt.plot([v.getY(), ev.getY()], [v.getX(), ev.getX()], Color='y')
    resetEdgeMark()
    
def heuristic_cost_estimate(node, goal):
    v_start = railroadNet[node]
    v_goal = railroadNet[goal]
    return calcdv(v_start, v_goal)

def getNodeWithLowestFScore(openSet, fScore):
    minValue = 9999999.00
    minNodeName = ''
    for nodeName in openSet:
        if fScore[nodeName] < minValue:
            minValue = fScore[nodeName]
            minNodeName = nodeName
    return minNodeName
                
def reconstruct_path(cameFrom, current, start):
    total_path = []
    if current != start:
        total_path.append(current)
        nextFrom = cameFrom[current]
        while nextFrom != start:
            total_path.insert(0, nextFrom)
            nextFrom = cameFrom[nextFrom]
    total_path.insert(0, start)
    return total_path

def aStarSearch(start, goal, fig, ax):
    # The set of nodes already evaluated (list date type)
    cloasedSet = []
    # The set of currently discovered nodes that are not evaluated yet.
    # Initially, only the start node is known.
    openSet = [start]
    # For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, cameFrom will eventually contain the
    # most efficient previous step.
    comeFrom = {} 
    # For each node, the cost of getting from the start node to that node.
    gScore ={}
    
    # For each node, the total cost of getting from the start node to the goal
    # by passing by that node. That value is partly known, partly heuristic.
    fScore = {}
    # set those f and g scores to very big value initially
    for name in nodeNames:
        if name != start:
            fScore[name] = 999999999.00
            gScore[name] = 999999999.00
            
    # For the first node, that value is completely heuristic.
    fScore[start] = heuristic_cost_estimate(start, goal)
    # The cost of going from start to start is zero.
    gScore[start] = 0.0
    previousPath = []
    currentPath = []
    while len(openSet) > 0:
        #time.sleep(0.5)
        printPath(previousPath, 'y')
        #the node in openSet having the lowest fScore[] value
        current = getNodeWithLowestFScore(openSet, fScore) 
        if current == goal:
            return reconstruct_path(comeFrom, current, start)

        openSet.remove(current)
        cloasedSet.append(current)
        circle = plt.Circle((railroadNet[current].getY(),railroadNet[current].getX()), 0.2, facecolor='green', edgecolor='black')
        ax.add_artist(circle)
        
        plt.pause(0.1)
        
        currentNode = railroadNet[current]
        previousPath = list(currentPath)
        printPath(previousPath, 'y')
        currentPath = reconstruct_path(comeFrom, current, start)
        printPath(currentPath, 'r')
        for edge in currentNode.getEdges():
            if edge.getFromNodeName() == current:
                neighbor = edge.getToNodeName()
            else:
                neighbor = edge.getFromNodeName()
            neighborNode = railroadNet[neighbor]
            
            if neighbor in cloasedSet:
                # Ignore the neighbor which is already evaluated.
                continue
            
            # Discover a new node
            if neighbor not in openSet:
                openSet.append(neighbor)
                circle = plt.Circle((railroadNet[neighbor].getY(),railroadNet[neighbor].getX()), 0.2, facecolor='blue', edgecolor='black')
                ax.add_artist(circle)
                plt.pause(0.1)
            # The distance from start to a neighbor
            tentative_gScore = gScore[current] + calcdv(currentNode, neighborNode)
            if tentative_gScore >= gScore[neighbor]:
                continue        # This is not a better path.

            # This path is the best until now. Record it!
            comeFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(neighbor, goal) 

    return [] # not found the path

def printPath(pathlist, clr):
    for index in range(1, len(pathlist)):
        preNode = railroadNet[pathlist[index-1]]
        curNode = railroadNet[pathlist[index]]
        plt.plot([preNode.getY(), curNode.getY()], [preNode.getX(), curNode.getX()], Color=clr)
        plt.pause(0.1)
                       
                       
def printPathWithDistance(pathlist, clr):
    total_distance = 0.0
    print("\nThe shortest path is: \n")
    print(railroadNet[pathlist[0]].getFullName() + "  ")
    for index in range(1, len(pathlist)):
        preNode = railroadNet[pathlist[index-1]]
        curNode = railroadNet[pathlist[index]]
        plt.plot([preNode.getY(), curNode.getY()], [preNode.getX(), curNode.getX()], Color=clr)
        plt.pause(0.1)
        d = calcdv(preNode , curNode  )
        total_distance += d
        print (curNode.getFullName() + ":" ,  d)
    print("The total distance of the path is:" ,  round(total_distance, 1))
                       
readNodes("romNodes.txt")
readFullName("romFullNames.txt")
readEdges("romEdges.txt")
# readNodes("rrNodes.txt")
# readNodeCity("rrNodeCity.txt")
# readEdges("rrEdges.txt")

displayDistance()
fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot()

ax.set_xlim(min(y_values)-0.2, max(y_values)+0.2)
ax.set_ylim(min(x_values)-0.2, max(x_values)+0.2)  
drawGraph(fig, ax)
start = cityNameMap[startName]
goal = cityNameMap[goalName]
pathlist = aStarSearch(start, goal, fig, ax)
printPathWithDistance(pathlist, 'red')
time.sleep(3)
fig.savefig(startName + "-" + goalName + '.png', dpi = 200)    
  



