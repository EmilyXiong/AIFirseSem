import os

currentNqme = input("Please enter your name:  ")
fileName = "savedAllName.txt"
allNames=[]
if os.path.exists(fileName):
    with open(fileName, "r") as fileInput:
        for preName in fileInput:
            allNames.append(preName.rstrip())
    fileInput.close()
    
if currentNqme not in allNames:
    allNames.append(currentNqme)

print ("List of names who has run this script: ", allNames)

with open(fileName, "w") as fileOutput:
    for item in allNames:
        fileOutput.write("%s\n" % item)
