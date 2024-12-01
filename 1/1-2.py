left = set()
right = []
sum = 0
with open("input.txt") as input:
    for line in input:
        pair = line.split()
        left.add(int(pair[0]))
        right.append(int(pair[1]))
    
for l in left:
    sum += right.count(l) * l

print(sum)