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
    return parsed

def moveStuff(stack, instructions):
    for i in instructions:
        new_i = parseInstruction(i)
        num = new_i["amount"]
        fr = new_i["from"]
        to = new_i["to"]
        for j in range(num):
            # move stuff

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
