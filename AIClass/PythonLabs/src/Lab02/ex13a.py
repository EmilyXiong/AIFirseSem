import sys

strInput = sys.argv[1]

strLen = len(strInput)
strDict={}

for index in range(0,  strLen-1):
    if strInput[index] in strDict:
        strDict[strInput[index]] = strDict[strInput[index]] + 1
    else:
        strDict[strInput[index]] = 1

mostCH=''
mostCount=0

for key, value in strDict.items():
    if strDict[key] > mostCount:
        mostCH = key
        mostCount = strDict[key]

print ("character " + mostCH + " has the most occurrentcs of ", mostCount)
        
