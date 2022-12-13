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
    return stack

def parseInstruction(instruction):
    text = instruction.split(" ")
    parsed = {"amount": text[1], "from": text[3], "to": text[5]}
    print(parsed)
    return parsed

def moveStuff(stack, instructions):
    for i in instructions:
        new_i = parseInstruction(i)
        num = int(new_i["amount"])
        fr = int(new_i["from"])
        to = int(new_i["to"])
       # continue
        for j in range(num):
            while(1):
                x = stack[fr - 1].pop()
                if x.startswith("["):
                    break
            # mam x
            stack[to - 1].append(x)

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
