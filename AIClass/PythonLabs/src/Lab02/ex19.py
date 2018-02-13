import sys

strInput = sys.argv[1]  
if strInput.isdigit():
    print ("This string contains only digit")
else:
    print ("This string contains non digit characters")