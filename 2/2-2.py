reports = []
safe = 0
with open("input.txt") as input:
    for line in input:
        report = [int(s) for s in line.split()]
        reports.append(report)

for report in reports:
    diffs = []
    s = 1
    damp = True
    for i, level in enumerate(report):
        if i + 1 == len(report):
            break
        diff = report[i + 1] - level
        diffs.append(diff)

    if diffs[0] < 0 and diffs[1] < 0:
        s = -1
    elif diffs[0] < 0 and diffs[2] < 0:
        s = -1
    elif diffs[1] < 0 and diffs[2] < 0:
        s = -1
        
    if s == -1:
        for i, d in enumerate(diffs):
            diffs[i] = d * s

    for i, d in enumerate(diffs):
        if d < 1 or d > 3:
            if not damp:
                break
            damp = False

            if i > 0:
                l =  diffs[i - 1] + d
                if 1 <= l <= 3:
                    pop = diffs.pop(i)
                    diffs[i - 1] = l
                    continue

            if i < len(diffs) - 1:
                r = d + diffs[i + 1]
                if 1 <= r <= 3:
                    pop = diffs.pop(i)
                    diffs[i] = r
                    continue

            if i == 0 or i + 1 == len(diffs):
                pop = diffs.pop(i)
                continue

            break
        i += 1

    for i, d in enumerate(diffs):
        if d < 1 or d > 3:
            break
        if i + 1 == len(diffs):
            safe += 1
print(safe)