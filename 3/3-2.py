import re

memory = []
muls = []
sum = 0
with open("input.txt") as input:
    memory = input.readlines()

for line in memory:
    muls.extend(re.findall("mul\(\d{1,3},\d{1,3}\)|do.?.?.?\(\)", line))

do = True
for i, string in enumerate(muls):
    match string:
        case "do()":
            do = True
        case "don't()":
            do = False
        case _:
            if do:
                muls[i] = re.findall("\d{1,3}", string)
                sum += int(muls[i][0]) * int(muls[i][1])

print(sum)