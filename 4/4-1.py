import re
crossword = []
xmaslist = []
with open("input.txt") as input:
    for line in input.readlines():
        crossword.append(re.findall("\S\S*", line)[0])

xmas = re.compile("(?=(XMAS|SAMX))")
x = len(crossword[0])
y = len(crossword)

for row in crossword:
    xmaslist.extend(xmas.findall(row))

for i in range(x):
    s = ""
    for row in crossword:
        s += row[i]
    xmaslist.extend(xmas.findall(s))

for y in range(y):
    diags = [""]*4
    for x in range(x):
        diags[0] += crossword[x][-(x+y)-1]
        diags[1] += crossword[x][x+y]
        diags[2] += crossword[x+y][x]
        diags[3] += crossword[x+y][-x-1]
    xmaslist.extend(xmas.findall(diags[0]))
    xmaslist.extend(xmas.findall(diags[1]))
    if y > 0:
        xmaslist.extend(xmas.findall(diags[2]))
        xmaslist.extend(xmas.findall(diags[3]))
    
print(len(xmaslist))