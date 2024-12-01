left = []
right = []
sum = 0
with open("input.txt") as input:
    for line in input:
        pair = line.split()
        left.append(int(pair[0]))
        right.append(int(pair[1]))
    left.sort()
    right.sort()
    
for (l,r) in zip(left, right):
    sum += abs(l - r)

print(sum)