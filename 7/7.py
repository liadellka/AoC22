class directory:
    name = ""
    stuff = []
    def __init__(self, name):
        self.name = name

    def addDir(self, dirName):
        newDir = directory(dirName)
        stuff.append(newDir)

    def addFile(self, fileName, size):
        newFile = {"name": fileName, "size", size}
        stuff.append(newFile)

    def getName(self):
        return self.name

    def getSub(self, name):


lines = []
with open("input.txt") as file:
    lines = file.readlines()

main = directory("/")
currentDirectory = main
previousDirectory = []
copy = False
for x in lines:
    if x == "$ cd /":
        previousDirectory.clear()
        currentDirectory = main
    elif x == "$ cd ..":
        currentDirectory = previousDirectory.pop()
    elif x.startswith("$ cd"):
        previousDirectory.append(currentDirectory)

    elif x == "$ ls":
        continue
    elif x.startswith("dir"):
        z = x.split(" ")
        currentDirectory.addDir(z[1])
    else:
        z = x.split(" ")
        currentDirectory.addFile(z[1], z[0])
