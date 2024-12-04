import re
crossword = []
sum = 0
with open("input.txt") as input:
    for line in input.readlines():
        crossword.append(re.findall("\S\S*", line)[0])

mas = re.compile("(?=(MAS|SAM))")
x = len(crossword[0])
y = len(crossword)

for i in range(1, x-1):
    for j in range(1, y-1):
        words = [""]*2
        if crossword[j][i] == "A":
            words[0] = crossword[j-1][i-1] + crossword[j][i] + crossword[j+1][i+1]
            words[1] = crossword[j-1][i+1] + crossword[j][i] + crossword[j+1][i-1]
        if bool(mas.search(words[0])) and bool(mas.search(words[1])):
            sum += 1

print(sum)