equations = []
sum = 0
with open("input.txt") as input:
    for line in input:
        equation = line.split()
        equations.append((int(equation[0].replace(":","")), [int(i) for i in equation[1:]]))

for equation in equations:
    for i in range(2 ** (len(equation[1]) - 1)):
        ans = 0
        i = f'{i:0{len(equation[1]) - 1}b}'
        for j, b in enumerate(i):
            if b == "0":
                if j == 0:
                    ans = equation[1][j] + equation[1][j+1]
                else:
                    ans += equation[1][j+1]
            if b == "1":
                if j == 0:
                    ans = equation[1][j] * equation[1][j+1]
                else:
                    ans *= equation[1][j+1]
        if ans == equation[0]:
            sum += ans
            break

print(sum)