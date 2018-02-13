import re
import random
import os

# GLOBAL VARIABLES
grid_size = 81

def isFull (grid):
    return grid.count('.') == 0
  
# can be used more purposefully
def getTrialCelli(grid):
  for i in range(grid_size):
    if grid[i] == '.':
      #print ('trial cell', i)
      return i
      
def isLegal(trialVal, trialCelli, grid):

  cols = 0
  for eachSq in range(9):
    trialSq = [ x+cols for x in range(3) ] + [ x+9+cols for x in range(3) ] + [ x+18+cols for x in range(3) ]
    cols +=3
    if cols in [9, 36]:
        cols +=18
    if trialCelli in trialSq:
        for i in trialSq:
            if grid[i] != '.':
                if trialVal == int(grid[i]):
                    return False
        break
  
  for eachRow in range(9):
    trialRow = [ x+(9*eachRow) for x in range (9) ]
    if trialCelli in trialRow:
        for i in trialRow:
            if grid[i] != '.':
                if trialVal == int(grid[i]):
                    return False
        break
  
  for eachCol in range(9):
    trialCol = [ (9*x)+eachCol for x in range (9) ]
    if trialCelli in trialCol:
        for i in trialCol:
            if grid[i] != '.':
                if trialVal == int(grid[i]):
                    return False
        break
    
  return True

def setCell(trialVal, trialCelli, grid):
  grid[trialCelli] = trialVal
  return grid

def clearCell( trialCelli, grid ):
  grid[trialCelli] = '.'
  #print ('clear cell', trialCelli)
  return grid

def printGrid (pzl):
    print ("\n------+------+------")   
    i = 0
    row = 0
    for row in range(0,9):
        col = 0
        line = ''
        for col in range(0, 9):
            line = line + str(pzl[i]) + ' '
            i += 1
            if (col % 3) == 2:
                line = line + '|'
        print (line)
        if (row % 3)==2:
            print ("------+------+------")     

def hasSolution (grid):
  if isFull(grid):
    return True
  else:
    trialCelli = getTrialCelli(grid)
    trialVal = 1
    solution_found = False
    while ( solution_found != True) and (trialVal < 10):
      #print ('trial valu',trialVal)
      if isLegal(trialVal, trialCelli, grid):
        grid = setCell(trialVal, trialCelli, grid)
        if hasSolution (grid) == True:
          solution_found = True
          return True
        else:
          clearCell( trialCelli, grid )
      #Sprint ('++')
      trialVal += 1
  return solution_found
# sampleGrid = ['2', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '3', '1', '.', '.', '.', '.', '9', '4', '.', '.', '.', '.', '7', '8', '2', '5', '.', '.', '4', '.', '.', '.', '.', '.', '.', '6', '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '8', '2', '.', '.', '.', '7', '.', '.', '9', '.', '.', '.', '.', '.', '.', '.', '.', '3', '1', '.', '4', '.', '.', '.', '.', '.', '.', '.', '3', '8', '.']

puzzle = '52...6.........7.13...........4..8..6......5...........418.........3..2...87.....'
sampleGrid = list(puzzle)

#sampleGrid = ['.', '.', '3', '.', '2', '.', '6', '.', '.', '9', '.', '.', '3', '.', '5', '.', '.', '1', '.', '.', '1', '8', '.', '6', '4', '.', '.', '.', '.', '8', '1', '.', '2', '9', '.', '.', '7', '.', '.', '.', '.', '.', '.', '.', '8', '.', '.', '6', '7', '.', '8', '2', '.', '.', '.', '.', '2', '6', '.', '9', '5', '.', '.', '8', '.', '.', '2', '.', '3', '.', '.', '9', '.', '.', '5', '.', '1', '.', '3', '.', '.']
#sampleGrid = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '4', '6', '2', '9', '5', '1', '8', '1', '9', '6', '3', '5', '8', '2', '7', '4', '4', '7', '3', '8', '9', '2', '6', '5', '1', '6', '8', '.', '.', '3', '1', '.', '4', '.', '.', '.', '.', '.', '.', '.', '3', '8', '.']
printGrid(sampleGrid)
if hasSolution (sampleGrid):
    printGrid(sampleGrid)
else: print ('NO SOLUTION')


