equations = []
sum = 0
with open("input.txt") as input:
    for line in input:
        equation = line.split()
        equations.append((int(equation[0].replace(":","")), [int(i) for i in equation[1:]]))

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(nums)

for equation in equations:
    for i in range(3 ** (len(equation[1]) - 1)):
        ans = 0
        i = f'{ternary(i):0{len(equation[1]) - 1}}'
        for j, b in enumerate(i):
            if b == "0":
                if j == 0:
                    ans = equation[1][j] + equation[1][j+1]
                else:
                    ans += equation[1][j+1]
            elif b == "1":
                if j == 0:
                    ans = equation[1][j] * equation[1][j+1]
                else:
                    ans *= equation[1][j+1]
            elif b == "2":
                if j == 0:
                    ans = int(str(equation[1][j]) + str(equation[1][j+1]))
                else:
                    ans = int(str(ans) + str(equation[1][j+1]))
            if ans > equation[0]:
                 break
        if ans == equation[0]:
             sum += ans
             break

print(sum)