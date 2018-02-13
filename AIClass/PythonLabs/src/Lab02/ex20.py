import sys
import re

strInput = sys.argv[1]  
legal_characters = '[10]+$'

if re.fullmatch(legal_characters, strInput):
    intValu = int(strInput, 2)
    print ("Decimal value is: ", float(intValu))
else:
    print ("Not a binary string!")