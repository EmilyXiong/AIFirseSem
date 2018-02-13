import sys

size = int(sys.argv[1])

faces = [[1,2,3,4,5],
         [1,11,12,17,18],
         [2,12,13,19,20],
         [3,13,14,21,22],
         [4,14,15,23,24],
         [5,15,11,25,16],
         [16,17,26,27,6],
         [7,18,19,27,28],
         [8,20,21,28,29],
         [9,22,23,29,30],
         [10,24,25,30,26],
         [6,7,8,9,10]]


usedEdges = []

def isInvalid(pos):
    for edge in faces[pos]:
        if edge in usedEdges:
            return True
    return False

def bruteForce(pzl):
    # returns a solved pzl or the empty string on failure
    if '.' not in pzl:
        return pzl 
    if pzl.count('Y') == size:
        return pzl 
    subPzl = pzl
    pos = pzl.find(".")
    if isInvalid(pos):
        subPzl = subPzl.replace('.', 'X', 1)
    else:
        subPzl = subPzl.replace('.', 'Y', 1)
        usedEdges.extend(faces[pos])
    BF = bruteForce(subPzl)
    if BF: return BF


puzzl = '............'
result =bruteForce(puzzl)
if result.count('Y') < size:
    print ("Imposible to find ", size, " faces that don't have common edges.")
else:
    print ("The selected faces are:" )
    for i in range(0, len(result)):
        if result[i] == 'Y':
            print(faces[i])
