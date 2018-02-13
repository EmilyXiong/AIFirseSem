import sys
from collections import OrderedDict

strInput = sys.argv[1]


strDict=OrderedDict()

for index in range(0,  len(strInput)):
    if strInput[index] in strDict:
        strDict[strInput[index]] = strDict[strInput[index]] + 1
    else:
        strDict[strInput[index]] = 1

for key, value in strDict.items():
    if strDict[key] == 1:
        print ("The first non repeating character is <" + key + ">")
        break
else:
    print ("There is no non repeating character")