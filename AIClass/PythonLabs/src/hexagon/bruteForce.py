import sys

sys.setrecursionlimit(15000)

puzzl = ['*10101*', '1010101', '0101010', '*01010*']

pattern1 = '101'
pattern2 = '010'

hexagonList = {}
triangleHexagonMap = {}


def isInvalid(pzl):
    temp = []
    for keyIndex in hexagonList:
        for triIndex in hexagonList[keyIndex]:
            temp.append(pzl[triIndex])
        for lable in temp:
            if lable != '.' and temp.count(lable) > 1:
                return True
    return False


def preparePuzzle():

    for i in range(0, 28):
        triangleHexagonMap[i] = []
        
    hcout = 0
    rowCount = len(puzzl)
    for i in range(0, rowCount-1):
        upRow =  puzzl[i]
        lowerRow = puzzl[i+1]
        indexU =upRow.index(pattern1)
        indexL = -1
        while indexU >=0:
            indexL = lowerRow.index(pattern2, indexL+1)
            if indexU == indexL:
                #find a hexagon
                hexagonList[hcout] = [i*7+indexU, i*7+indexU+1, i*7+indexU+2, (i+1)*7+indexL, (i+1)*7+indexL+1, (i+1)*7+indexL+2]
                triangleHexagonMap[i*7+indexU].append(hcout)
                triangleHexagonMap[i*7+indexU+1].append(hcout)
                triangleHexagonMap[i*7+indexU+2].append(hcout)
                triangleHexagonMap[(i+1)*7+indexL].append(hcout)
                triangleHexagonMap[(i+1)*7+indexL+1].append(hcout)
                triangleHexagonMap[(i+1)*7+indexL+2].append(hcout)
                hcout +=1
                if pattern1 in upRow[indexU+1:]:
                    indexU = upRow.index('101', indexU+1)
                else:
                    indexU = -1

def bruteForce(pzl):
    # returns a solved pzl or the empty string on failure
    if isInvalid(pzl): return ""
    if '.' not in pzl: return pzl 
    for lable in range (1, 7):
        subPzl = pzl
        subPzl.replace('.', str(lable), 1)
        bF = bruteForce(subPzl)
        if bF:  return pzl
        return ""
        


preparePuzzle()
emptyPzl = "*.....*..............*.....*"
result = bruteForce(emptyPzl)

print (result)
