
def getSame(a, b):
    print("Cast a:", a)
    print("Cast b:", b)
    for x in a:
        if x in b:
            return x
    return None

def getRes(lines):
    res = 0
    i = 0
    for l in lines:
        ln =int(len(l) / 2)
        part1 = l[:ln]
        part2 = l[ln:]
        x = getSame(part1, part2)
        print("radek cislo: ",i,"Hodnota: ",x)
        ax = ord(x)
        if ax < 92:
            ax -= 38
        else:
            ax -= 96
        res += ax
        i += 1
    return res    

def getBadge(a, b, c):
    for x in a:
        if x in b and x in c:
            return x
    return None


def getBadgesRes(lines):
    res = 0
    i = 0
    length = len(lines)
    while i < length:
        b = getBadge(lines[i], lines[i+1], lines[i+2])
        bx = ord(b)
        if bx < 92:
            bx -= 38
        else:
            bx -= 96
        res += bx
        i += 3
    return res



lines = []
with open('input.txt') as file:
    lines = file.readlines()

res = getRes(lines)
bad = getBadgesRes(lines)

print(res)
print("Badges: ", bad)
