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

def validateOrder(update):
    b = True
    for n, page in enumerate(update):
        valid = ruledict.get(page, [])
        for m, p in enumerate(update[n+1:]):
            if p not in valid:
                update.insert(m, update.pop(n+m+1))
                b = False
    return b
        
for update in updates:
    order = validateOrder(update)
    if order:
        continue
    i = 0
    while not order:
        order = validateOrder(update)
        i += 1
    if order:
        mid = len(update) // 2
        sum += int(update[mid])
    else:
        print("Validation Failed!")
        break

print(sum)