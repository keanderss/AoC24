reports = []
safe = 0
with open("input.txt") as input:
    for line in input:
        report = [int(s) for s in line.split()]
        if report[0] > report[-1]:
            report.reverse()
        reports.append(report)

for report in reports:
    for i, level in enumerate(report):
        if i + 1 == len(report):
            safe += 1
            break
        diff = report[i + 1] - level
        if diff < 1 or diff > 3:
            break

print(safe)