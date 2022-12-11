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
    return stack


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

