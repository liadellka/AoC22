def overlaps(l):
    x = l.split(",")
    y = x[0].split("-")
    z = x[1].split("-")
    a = int(y[0])
    b = int(y[1])
    c = int(z[0])
    d = int(z[1])
    # ab obsahuje cd
    if a <= c and b >= d:
        return True
    elif a >= c and b <= d:
        return True
    elif a <= c and c <= b:
        return True
    elif a <= d and d <= b:
        return True
    else:
        return False

def getRes(lines):
    count = 0
    for l in lines:
        if overlaps(l):
            count += 1
    return count

lines = []
with open('input.txt') as file:
    lines = file.readlines()

res = getRes(lines)
print("Overlaps: ", res)
