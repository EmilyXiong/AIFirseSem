import sys
from collections import OrderedDict

strInput = sys.argv[1]

strDict=OrderedDict()
outStr = ''
for index in range(0,  len(strInput)):
    if strInput[index] not in strDict:
        strDict[strInput[index]] = 1
        outStr += strInput[index]
        
print (outStr)
    