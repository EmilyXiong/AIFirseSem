
def matchTwoWords(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        diffCount = 0
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                diffCount += 1
                if diffCount >1:
                    return False
        else:
            if diffCount == 1:
                return True
            else:
                return False

def matchWordWithGroup(word, group):
    for g_word in group:
        if matchTwoWords(word, g_word):
            return [word, g_word]
    else:
        return None
 
#read words into a list
allWords = []
with open("words.txt", "r") as wordFile:
    for line in wordFile:
        allWords.append(line.rstrip())
        
groups=[]
while len( allWords) > 0: #while allWords isn't empty
    word = allWords[0]
    allWords.remove(word)
    for group in groups:
            old_group = matchWordWithGroup(word, group)
            if old_group != None:
                group.append(word)
                break
    else:
        new_group = matchWordWithGroup(word, allWords)
        if new_group != None:
            groups.append(new_group)  #create a new group and add it groups
            allWords.remove(new_group[1])
        else:
            groups.append([word])        
            
for group in groups:
    print(group)

print ("There are total ", len(groups), " groups")
                

            
    
    