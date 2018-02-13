import sys

strInput = sys.argv[1]
inList = strInput.split(' ', 1)

index = 0
outStr=''
while(index < len(inList[1])):
    pos = inList[1].find(inList[0], index)
    if pos > 0:
        outStr += str(pos) + ","
        index = pos+1
    else:
        break

if outStr != '':
    print ("found at positions " + outStr[0:len(outStr)-1])
else:
    print("not found !")