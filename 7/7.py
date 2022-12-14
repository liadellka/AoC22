class directory:
    name = ""
    stuff = []
    size = 0
    def __init__(self, name):
        self.name = name

    def addDir(self, dirName):
        newDir = directory(dirName)
        self.stuff.append(newDir)

    def addFile(self, fileName, size):
        newFile = {"name": fileName, "size": size}
        self.stuff.append(newFile)
        self.size += int(size)

    def getName(self):
        return self.name

    def getSub(self, name):
        for x in self.stuff:
            if type(x) == directory:
                if x.getName() == name:
                    return x
    def getSize(self):
        # size = 0
        # for x in self.stuff:
          #  if type(x) == directory:
           #     size += x.getSize()
            #else:
             #   size += int(x["size"])
        return self.size


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
        currentDirectory.addDir(z[1])
    else:
        z = x.split(" ")
        currentDirectory.addFile(z[1], z[0])

print(main)
print("Velikost domovske slozky: ", main.getSize())
