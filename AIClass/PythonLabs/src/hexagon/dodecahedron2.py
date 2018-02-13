import sys

size = int(sys.argv[1])

faces = [         [1,11,12,17,18],

        [1,2,3,4,5],
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

all_colors = ['r', 'b', 'y', 'g', 'w', 'p', 'o']

used_color = all_colors[0:size]

def borders(f1, f2):
    if list(set(f1) & set(f2)):
        return True
    else:
        return False
        
def isInvalid(pzl): 
    for i in range(0, len(pzl)):
        if pzl[i] == '.':
            return False
        for j in  range(0, len(pzl)):
            if i != j and borders(faces[i], faces[j]):
                if pzl[i] == pzl[j]:
                    return True
    return False

def bruteForce(pzl):
    # returns a solved pzl or the empty string on failure
    if isInvalid(pzl): 
        return ""
    if '.' not in pzl:
        return pzl 
    for clr in used_color:
        subPzl = pzl
        subPzl = subPzl.replace('.', clr, 1)
        bF = bruteForce(subPzl)
        if bF:  return bF
    return ""

puzzl = '............'
result =bruteForce(puzzl)
if not result:
    print ("Imposible to use ", size, " colors to color all faces that no two faces that share a common edge are allowed to have the same color.")
else:
    clrCount = list(set(result))
    print ("We have used :", len(clrCount), " colors:" , clrCount)
    print ("The faces have colored as:", result)

