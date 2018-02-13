import sys

sys.setrecursionlimit(15000)

hexagonList = [ [1, 2, 3, 8, 9, 10], [3, 4, 5, 10, 11, 12], [7, 8, 9, 14, 15, 16], [9, 10, 11, 16, 17, 18],  [11, 12, 13, 18, 19, 20], [15, 16, 17, 22, 23, 24],  [17, 18, 19, 24, 25, 26]]
triRows = [[1,2,3,4,5], [7,8,9,10,11,12,13], [14,15,16,17,18,19,20], [22,23,24,25,26],
           [1,2,7,8,14], [3,4,9,10,15,16,22], [5,11,12,17,18,23,24], [13,19,20,25,26],
           [7,14,15,22,23], [1,8,9,16,17,24,25], [2,3,10,11,18,19,26],[4,5,12,13,20] ]
       
def hasSameNumber(triIndeies, pzl):  
    temp = []
    for  triIndex in triIndeies:
        temp.append(pzl[triIndex])
    for lable in temp:
        if lable != '.' and temp.count(lable) > 1:
            return True
    return False
       
def isInvalid(pzl):
    for hexagon in hexagonList:
        if hasSameNumber(hexagon, pzl):
            return True
    for triRow in triRows:
        if hasSameNumber(triRow, pzl):
            return True
    return False


def bruteForce(pzl):
    # returns a solved pzl or the empty string on failure
    if isInvalid(pzl): return ""
    if '.' not in pzl: return pzl 
    for lable in range (1, 7):
        subPzl = pzl
        subPzl = subPzl.replace('.', str(lable), 1)
        bF = bruteForce(subPzl)
        if bF:  return bF
        return ""

# '*.....*..123....456..*.....*'
emptyPzl = '*.....*..............*.....*'
result = bruteForce(emptyPzl)
if result:
    print ("The result is: <", result, ">\n\n")
    print(result[0:7])
    print(result[7:14])
    print(result[14:21])
    print(result[21:])

