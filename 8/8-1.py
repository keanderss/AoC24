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

for char in charset:
    cords = charmap[char]
    for i, cord in enumerate(cords):
        for c in cords[1+i:]:
            dx = c[0] - cord[0]
            dy = c[1] - cord[1]
            nodes = (cord[0] - dx, cord[1] - dy),(c[0] + dx, c[1] + dy)
            for node in nodes:
                if 0 <= node[0] < len(matrix[0]) and 0 <= node[1] < len(matrix):
                    anti_nodes.add(node)

print(len(anti_nodes))