import sys

strInput = sys.argv[1]
wordList = strInput.split()
vowelList = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'I', 'O', 'U']
outStr = []
counter = 0
for word in wordList:
    for ch in word:
        if ch in vowelList:
            counter += 1
    if counter >= 3:
        outStr.append(word)
    counter = 0

print ("These are the words that have at least three vowels: ", outStr)
    