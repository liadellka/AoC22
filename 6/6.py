def check(string):
    for i in range(4):
        for j in range(i + 1, 4):
            if string[i] == string[j]:
                return False
    return True
          
def message(string):
    for i in range(14):
        for j in range(i+1, 14):
            if string[i] == string[j]:
                return False
    return True

lines = []
with open("input.txt") as file:
    lines = file.readlines()

i = 0
line = lines[0]
for x in line:
    string = line[i:i+4]
    if check(string):
        print(i, "je pozice prvniho a ", i + 3, " pozice posledniho znaku")
        break
    else:
        i += 1

i = 0
for x in line:
    string = line[i:i+14]
    if message(string):
        print("pozice posledniho je: ",i+14)
        break
    else:
        i += 1
