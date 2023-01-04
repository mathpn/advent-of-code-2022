import re

input = open("input.txt").read().splitlines()

instructions = []
stacks = [[] for _ in range((len(input[0]) + 1) // 4)]

regex = re.compile("move (\d+) from (\d+) to (\d+)")
for row in input:
    if row.startswith("move"):
        instructions.append([int(x) for x in regex.search(row).groups()])
    else:
        row = [row[i : i + 4] for i in range(0, len(row), 4)]
        for i, crate in enumerate(row):
            crate = crate.strip()
            if crate and crate.startswith("["):
                stacks[i].append(re.sub("[^A-Z]", "", crate))

for quantity, origin, destiny in instructions:
    origin -= 1
    destiny -= 1
    move = stacks[origin][:quantity]
    stacks[origin] = stacks[origin][quantity:]
    stacks[destiny] = move[::-1] + stacks[destiny]

print("".join([stack[0] for stack in stacks]))
