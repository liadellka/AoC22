lines = []
input = []
with open('input.txt') as file:
    lines = file.readlines()
count = 0
for l in lines:
    if l == "\n":
        input.append(count)
        count = 0
        continue
    count += int(l)

# for x in input:
#    print(x)
print("Max input of the eleves: ", max(input))

input.sort()
input.reverse()
max_count = 0
for x in range(3):
    print(input[x])
    max_count += input[x]

print("In total they carry: ", max_count)
