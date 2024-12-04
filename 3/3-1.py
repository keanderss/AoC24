import re

memory = []
muls = []
sum = 0
with open("input.txt") as input:
    memory = input.readlines()

for line in memory:
    muls.extend(re.findall("mul\(\d{1,3},\d{1,3}\)", line))

for i, y in enumerate(muls):
    muls[i] = re.findall("\d{1,3}", y)
    sum += int(muls[i][0]) * int(muls[i][1])

print(sum)