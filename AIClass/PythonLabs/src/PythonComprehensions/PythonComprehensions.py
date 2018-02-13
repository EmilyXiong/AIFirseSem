### 1. Find one line expression for 
###    {0, 9, 10, 19, 20, 29, 30, 39, 40, 49, 50, 59, 60, 69, 70, 79, 80, 89, 90, 99}

set((sorted(set(range(0, 100, 10)) | set(range(9, 100, 10)))))

### 2.Same as above except have at most moe usage of set(), {}, and [] in total

set(sorted({x for x in range(0, 100, 10)} | set([x for x in range(9, 100, 10)])))

###############################################################################################################
###   Suppose the vertices of a graph are given 1, 2, 3, 4, ... n while there are edges between any two 
###   vertices whos labels sum to a perfect square.
###############################################################################################################
### 3. Create a python data structure representing such a graph in one line in O(n**2) time.
n = 10
print( {i:[j for j in range(1, n+1) if (i+j)**.5 == int((i+j)**.5)] for i in range(1, n+1)})

### 4. Create a python data structure representing such a graph in two lines in O(n**1.5) time.
# f={x+y for x in range(1, n+1) for y in range(1, n+1)}
# print( {i:[j for j+i in f if (i+j)**.5 == int((i+j)**.5)] for i in range(1, n)})

###############################################################################################################
###   Consider an n x n chessboard labelled with numbers 0, 1, ... n**2 -1.
###############################################################################################################
### 5. For each square , find all the other squares in the same row and same column as the given square.
n = 4

{s:({x for x in range((s-int(s%n)), s+n-int(s%n)) if x != s} | {x for x in range((int(s%n)), n*n, n) if x != s}) for s in range (0, n*n)}

### 6. For each square, find the squares imediately adjacent to it, both horizontally and vertically, but not diagonally.

print ({s:(set([s-n]) if int(s/n) >0 else set([])) | (set([s+n]) if int(s/n) < n-1 else set([])) | (set([s-1]) if int(s%n)>0 else set([])) | (set([s+1]) if int(s%n)<n-1 else set([])) for s in range(0, n*n)})

###############################################################################################################
###   Given a set of integers( that is, all integers from the sequence {0, 1, 2, 3, 4, ... , mx-1} 
###   and a list, cl, of sets containing those integers (where any integer may be contained in more than one set)
###############################################################################################################

### 7. Find a one line expression for a list of length  mx where the item at index k is the set of 
###    indices from cl such that integer k appears in the corresponding set in cl. Ie. Which sets of cl is k in 
mx = 10
cl = [(1,3,5,6,8), (2,4,7,9,), (2,6,8,9), (1,3,9,5), (4,8,7,9,0), (0, 3,7,9)]
solution = [{i for i,x in enumerate(cl) if j in x} for j in range(0, mx)]
print (solution)

### 8. Find a one line expression for a list of length mx where the item at index k is a set of all those integers 
###    such that k and that integer are both in at least one set from cl.

solution =  [set([item for sublist in [x for i,x in enumerate(cl) if j in x] for item in sublist]) for j in range(0, 6)]
print (solution)



###############################################################################################################
### Given a game table, represented by the list game (ie. game is an 8 x 8 table converted with certain playing 
### pieces (eg. chess or checkers. Sudoku would be a 9 x 9 example), implemented as a list, a translation table 
### is alist of a permutation of the integers from 0 to 8**2 -1 = 63/ For example, a simple translation would 
### be to move each item to the position that is one greater than it. and move the lst item to the first position. 
### This could be given by xlate = [63, 0, 1, 2, 3, 4, ... , 62]
###############################################################################################################

###  9. Write doen xlate as a one line python list comprehension.
xlate=list(range(0, n*n))
print (xlate)

### 10. Use xlate to translate the game in one line to newGame
### this is a example to swap position at index 0 and 1. It should result in a new game

xlate[0], xlate[1] = xlate[1], xlate[0]
print (xlate)

### 11. Write down a python one line translation table to implement rotation by 180 degree.
xlate = list(reversed(xlate))
print (xlate)

### 12. Write down a python one line translation table to implement a flip about the vertical axis
xlate = [item for sublist in [list(reversed( [xlate[x:x+n] for x in range(0, n*n, n)][i])) for i in range(0, n)] for item in sublist]
print (xlate)

### 13. Write down a python one line translation table to implement a 90 degree clockwise (CW) rotation.
xlate = [item for sublist in list(list(reversed([xlate[x] for x in range(i, 16, 4)])) for i in range(0, 4)) for item in sublist]
print (xlate)

