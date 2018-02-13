import sys

strInput = sys.argv[1]
inList = strInput.split(' ', 2)

outStr= inList[2].replace(inList[0], inList[1])
print(outStr)