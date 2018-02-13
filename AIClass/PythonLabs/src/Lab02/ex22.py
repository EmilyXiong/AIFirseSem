import sys

strInput = sys.argv[1].split()
for word in strInput:
    print (word[::-1])