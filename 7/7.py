class directory:
    name = ""
    stuff = []
    size = 0
    def __init__(self, name):
        self.name = name

    def addDir(self, dirName):
        newDir = directory(dirName)
        self.stuff.append(newDir)
        print("Adding directory: ", dirName)

    def addFile(self, fileName, size):
        newFile = {"name": fileName, "size": size}
        self.stuff.append(newFile)
        self.size += int(size)
        print("Adding file: ", fileName, " with size: ", size)

    def getName(self):
        return self.name

    def getSub(self, name):
        for x in self.stuff:
            if type(x) == directory:
                if x.getName() == name:
                    return x
    def getSize(self):
        return self.size

    def isEmpty(self):
        empty = self.stuff == []
        return empty

    def printDir(self):
        for x in self.stuff:
            if type(x) == directory:
                if x.isEmpty():
                    print("Directory: ", x.getName)
                else:
                    x.printDir()
            else:
                print("file: ", x["name"])

lines = []
with open("input.txt") as file:
    lines = file.readlines()

main = directory("/")
currentDirectory = main
previousDirectory = []
copy = False
for x in lines:
    if x == "$ cd /\n":
        previousDirectory.clear()
        currentDirectory = main
    elif x == "$ cd ..\n":
        currentDirectory = previousDirectory.pop()
    elif x.startswith("$ cd"):
        previousDirectory.append(currentDirectory)
        y = x.split(" ")
        newDir = currentDirectory.getSub(y[2])
    elif x == "$ ls\n":
        continue
    elif x.startswith("dir"):
        z = x.split(" ")
        currentDirectory.addDir(z[1].strip())
    else:
        z = x.split(" ")
        currentDirectory.addFile(z[1].strip(), z[0])

print(main)
print("Velikost domovske slozky: ", main.getSize())
# main.printDir()
for x in main.getStuff():
    print(x)