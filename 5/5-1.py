import re
rules = []
ruledict = {}
updates = []
sum = 0
with open("input.txt") as input:
    for line in input.readlines():
        rule = re.findall("\d\d*\|\d\d*", line)
        update = re.findall("\d\d*,.*\d\d*", line)
        if rule:
            rules.append(str(rule[0]).split("|"))
        if update:
            updates.append(str(update[0]).split(",")[::-1])

for rule in rules:
    ruledict[rule[1]] = []

for rule in rules:
    ruledict[rule[1]].append(rule[0])

for update in updates:
    order = True
    for n, page in enumerate(update):
        valid = ruledict.get(page, [])
        for p in update[n+1:]:
            if p not in valid:
                order = False
                break
        if not order:
            break
    if order:
        mid = len(update) // 2
        sum += int(update[mid])

print(sum)