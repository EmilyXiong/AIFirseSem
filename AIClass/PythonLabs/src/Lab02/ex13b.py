import sys

strInput = sys.argv[1]
strLen = len(strInput)
strDict={}

for index in range(0,  strLen):
    if strInput[index] in strDict:
        strDict[strInput[index]] = strDict[strInput[index]] + 1
    else:
        strDict[strInput[index]] = 1
        
#find the max value in the dictionary
maxOccur = max([ j for j in strDict.values()]) 

#go through the dictionary and put all characters with max occurance into a list 

strOut = ""
for key, value in strDict.items():
    if strDict[key] == maxOccur:
        strOut += key + ", " 
        

print ("characters " + strOut + " has the most occurrentcs of ", maxOccur)
        
