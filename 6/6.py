def check(string):
    for i in range(4):
        for j in range(i + 1, 4):
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

