def getVal(input):
    if input == "X" or input == "A":
        return 1
    if input == "Y" or input == "B":
        return 2
    if input == "Z" or input == "C":
        return 3
   

def switchToSame(me):
    if me == "X":
        return "A"
    if me =="Y":
        return "B"
    if me == "Z":
        return "C"
    

def getMyPoints(op, me):
    me_abc = switchToSame(me)

    if op == me_abc:
        return 3
    # vyhry - moje -> on papir, já nuzky; on nuzky, ja kamen; on kamen, ja papi
    if op == "B" and me_abc == "C":
        return 6
    if op == "C" and me_abc == "A":
        return 6
    if op == "A" and me_abc == "B":
        return 6
    
    return 0

def part2(op, res):
    if res == "X":
        if op == "B":
            return getVal("A")
        if op == "C":
            return getVal("B")
        if op == "A":
            return getVal("C")

    if res == "Y":
        return (3 + getVal(op))

    if res == "Z":
        if op == "B":
            return (6 + getVal("C"))
        if op == "C":
            return (6 + getVal("A"))
        if op == "A":
            return (6 + getVal("B"))

lines = []
with open('input.txt') as file:
    lines = file.readlines()

result = 0
for l in lines:
    # result += getVal(l[2])
    # result += getMyPoints(l[0], l[2])
    result += part2(l[0], l[2])

print(result)
