import re
matrix = []
cs = []
charmap = {}
charset = set()
anti_nodes = set()
with open("input.txt") as input:
    for y, line in enumerate(input.readlines()):
        line = list(re.findall("\S\S*", line)[0])
        matrix.append(line)
        for x, char in enumerate(line):
            if char != ".":
                charmap[char] = []
                charset.add(char)
                cs.append([char, (x,y)])
    for char in cs:
        charmap[char[0]].append(char[1])

def getNodes(x, y, s):
    nodes = []
    node = (0, 0)
    i = 1
    while 0 <= node[0] < len(matrix[0]) and 0 <= node[1] < len(matrix):
        node = (x + s * dx * i, y + s * dy * i)
        if 0 <= node[0] < len(matrix[0]) and 0 <= node[1] < len(matrix):
            nodes.append(node)
        i += 1
    return nodes

for char in charset:
    cords = charmap[char]
    for i, cord in enumerate(cords):
        for c in cords[1+i:]:
            dx = c[0] - cord[0]
            dy = c[1] - cord[1]
            nodes = getNodes(cord[0], cord[1], -1)
            nodes.extend(getNodes(c[0], c[1], 1))
            for node in nodes:
                if matrix[node[1]][node[0]] == ".":
                    matrix[node[1]][node[0]] = "#"
                anti_nodes.add(node)

for node in cs:
    anti_nodes.add(node[1])

for line in matrix:
    for c in line:
        print(c, end="")
    print("")

print(len(anti_nodes))