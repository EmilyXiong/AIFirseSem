import sys

str1 = sys.argv[1]
str2 = sys.argv[2]

if ' '.join(sorted(str1)) == ' '.join(sorted(str2)):
    print("'" + str1 + "' and '" + str2 + "' are anagrams of each other")
else:
    print("'" + str1 + "' and '" + str2 + "' are NOT anagrams of each other")