import sys

strInput = sys.argv[1]

maxDiff = 0
pos = 0
for index in range(0,  len(strInput)-1):
    diff = abs(ord(strInput[index+1]) - ord(strInput[index]))
    if diff > maxDiff:
        maxDiff = diff
        pos = index

print ("This adjacent pair <" + strInput[pos] + strInput[pos+1] + "> has greatest difference between their ascii values")