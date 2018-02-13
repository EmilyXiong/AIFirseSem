from vertice import vertice
from distanceDemo import calcd, calcdv
import matplotlib.pyplot as plt

railroadNet = {}
shortNames=[]
#open romNodes.txt to read in vertices

#read in romNodes.txt to build the graph with vertices
x_values =[]
y_values = []
with open("romNodes.txt", "r") as nodeFile:
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
        shortNames.append(line[0])
        
#Now open file romFullName.txt to add the full names to vertices
with open("romFullNames.txt", "r") as fullNameFile:
    index = 0
    for line in fullNameFile:
        v = railroadNet[shortNames[index]]
        v.setFullName(line.rstrip())
        index += 1
        
#Open romEdges.txt to build edges for each vertice
with open("romEdges.txt", "r") as edgesFile:
    index = 0
    for line in edgesFile:
        vs = line.rstrip().split(' ')
        v0 = railroadNet[vs[0]]
        v1 = railroadNet[vs[1]]
        v0.addEdge(vs[1])
        
#calculate edge distance
sumD = 0.0
for name in shortNames:
    v = railroadNet[name]
    for edgeName in v.getEdges():
        ev = railroadNet[edgeName]
        d = calcdv(v, ev)
        sumD += d
        print("edge between " + v.getName() + " and " + ev.getName() + " is: ", d)

print("Sum of all edges are:", round(sumD,1))

#draw graph 
fig, ax = plt.subplots()
ax.set_xlim(min(y_values)-0.2, max(y_values)+0.2)
ax.set_ylim(min(x_values)-0.2, max(x_values)+0.2)
for name in shortNames:
    v = railroadNet[name]
    #class matplotlib.pyplot.Circle(xy, radius=5, **kwargs)
    circle = plt.Circle((v.getY(),v.getX()), 0.2, facecolor='y', edgecolor='b')
    plt.text(v.getY()-0.1, v.getX(),v.getName())
    for edgeName in v.getEdges():
        ev = railroadNet[edgeName]
        plt.plot([v.getY(), ev.getY()], [v.getX(), ev.getX()], Color='y')

    ax.add_artist(circle)

    
fig.savefig('plotcircles.png', dpi = 200)    
