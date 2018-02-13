import sys
import re

strInput = sys.argv[1]  
legal_characters = '[0-9a-fA-F]+$'

if re.fullmatch(legal_characters, strInput):
    intValu = int(strInput, 16)
    print ("Decimal value is: ", float(intValu))
else:
    print ("Not a Hex string!")