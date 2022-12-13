def removeBlank(s):
    while(1):
        if s[-1].startswith("["):
            break
        else:
            s.pop()

def parseText(stack_txt):
    stack = []
    for s in stack_txt:
        a = 0
        if s.startswith(" 1"):
            break
        for i in range(9):
            x = s[a:a+3]
            a += 4
            if len(stack) <= i:
                y = []
                stack.append(y)
                stack[i].append(x)
            else:
                stack[i].append(x)
    for s in stack:
        s.reverse()
        s = removeBlank(s)
    return stack

def parseInstruction(instruction):
    text = instruction.split(" ")
    parsed = {"amount": text[1], "from": text[3], "to": text[5]}
    print(parsed)
    return parsed

def getStuff(stack, number):
    x = []
    y = ""
    while(1):
        y = stack.pop()
        print("Y= ",y)
        if y.startswith("["):
            break
            print("Here")
    for i in range(number):
        if y == "":
            y = stack.pop()
        x.append(y)
        y = ""
    x.reverse()
    return x

def moveStuff(stack, instructions):
    for i in instructions:
        new_i = parseInstruction(i)
        num = int(new_i["amount"])
        fr = int(new_i["from"])
        to = int(new_i["to"])
       # part one
      #  for j in range(num):
       #     while(1):
        #        x = stack[fr - 1].pop()
         #       if x.startswith("["):
          #          break
            # mam x
           # stack[to - 1].append(x)
        y = getStuff(stack[fr - 1], num)
        for z in y:
            stack[to - 1].append(z)

def printTop(s):
    for x in s:
        y = x[-1]
        print(y[1], end='')


lines = []
with open('input.txt') as f:
    lines = f.readlines()
stack = []
i = 0
for l in lines:
    if l == "\n":
        i += 1
        break
    stack.append(l)
    i += 1
instructions = lines[i:]
# print("stack:")
# print(stack)
# print("instructions:")
# print(instructions)

s = parseText(stack)
print(s)

moveStuff(s, instructions)
print("After moving:")
printTop(s)
