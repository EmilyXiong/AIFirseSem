import time
import sys
from vertice import Vertice

# This function is from https://stackoverflow.com/questions/25216328/compare-strings-allowing-one-character-difference
# By: Marco Sulla

def matchTwoWords(s1, s2):
    ok = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if ok:
                return False
            else:
                ok = True

    return ok

def matchWordWithGroup(word, group):
    for g_word in group:
        if matchTwoWords(word, g_word):
            
            return [word, g_word]
    else:
        return None
 
#read words into a list
allWords = []
wordfileName = "words.txt"
startTime = time.time()

with open(wordfileName, "r") as wordFile:
    for line in wordFile:
        allWords.append(line.rstrip())
        


# check if an argument exist
in_word = ''
if len(sys.argv) > 1:
    in_word = sys.argv[1]
    if len(in_word) != 6:
        print ("you have given a wrong argument. the input word must be 6 character long")
        sys.exit()
    if in_word not in allWords:
        print ("you have entered a word which isn't in the word file;")
        sys.exit()

graphDic={}
edgeCount = 0
groupId = 0

while len( allWords) > 0: #while allWords isn't empty
    word = allWords[0]
    allWords.remove(word)
    v_new = Vertice(word)
    for v_word in graphDic:
        if matchTwoWords(word, v_word):
            v_new.add_edge(v_word)
            graphDic[v_word].add_edge(word)
            if v_new.getGroupId() == 0:
                v_new.setGroupId(graphDic[v_word].getGroupId())
            else:
                graphDic[v_word].setGroupId(v_new.getGroupId())
            edgeCount += 1
    if v_new.getGroupId() == 0:
        groupId += 1
        v_new.setGroupId(groupId)
    graphDic[word] = v_new

timeReadbuild = time.time() - startTime


verticsCount = 0
mostEdge = 0
mostEdgeList =[]
for v_key in graphDic:
    edges = len(graphDic[v_key].getEdges())
    if edges > 0:
        verticsCount += 1
    if edges > mostEdge:
        mostEdge = edges
        mostEdgeList =[v_key]
    elif edges == mostEdge:
        mostEdgeList.append(v_key)
        
components = {}
for v_key in graphDic:
    groupId = graphDic[v_key].getGroupId()
    if groupId not in components:
        components[groupId] = [v_key]
    else:
        components[groupId].append(v_key)
        
comCount = 0
maxCount = 0
maxGoupId = 0

for gid in components:
    vCount = len(components[gid])
    if vCount > 1:
        comCount += 1
    if vCount > maxCount:
        maxCount = vCount
        maxGoupId = gid
        
timeRun = time.time() - startTime
  
print("A: The number of vertices in the graph", verticsCount)

print("B: The number of edges in the graph", edgeCount )

if in_word != '':              
    v_seek = graphDic[in_word]
    if len(v_seek.getEdges()) > 0:
        print("C: The work " + in_word + " has the following neighbors:", v_seek.getEdges())
    else:
        print("C: The work " + in_word + " doesn't have any neighbor:")


print("D: Total time reading the file is : ", timeReadbuild)

print("E: Total time running building the graph is : ", timeRun)
print("F: The word(s) with the most neighbors are: ", mostEdgeList)
print("The number of neighbors those words have is : ", mostEdge)



print("G: we have total of ", comCount , " connected components in the graph.")
print("H: the largest size of connected component has ", maxCount, " Vertices. Those words are:")
print(components[maxGoupId])


    
    