import os

currentNqme = input("Please enter your name:  ")
fileName = ("savedName.txt")
preName=''
if os.path.exists(fileName):
    with open(fileName, "r") as fileInput:
        preName=fileInput.readline()
    fileInput.close()
    
if preName == '':
    print ("you are the first person runing this script.")
else:
    print ("The previous person's name who run this script was: " + preName)

with open(fileName, "w") as fileOutput:
    fileOutput.write(currentNqme)