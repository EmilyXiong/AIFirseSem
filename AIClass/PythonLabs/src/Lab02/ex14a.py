import sys

strInput = sys.argv[1]
wordList = strInput.split()
vowelList = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'I', 'O', 'U']
outStr = []
for word in wordList:
    if word[0] in vowelList and word[len(word) -1] in vowelList:
        outStr.append(word)
print ("These are the words start and end with vowel: ", outStr)