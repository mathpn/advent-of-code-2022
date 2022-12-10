input = open('input.txt').read().splitlines()

points = {"X": 1, "Y": 2, "Z": 3}
choices = ["A", "B", "C"]


strategies = [row.split(' ') for row in input]

total = 0
for oponent, mine in strategies:
    mine = points[mine]
    oponent = choices.index(oponent)
    if oponent + 1 == mine:
        total += 3 + mine
        continue
    if (3 + oponent + 1) % 3 + 1 == mine:
        total += 6 + mine
    else:
        total += mine

print(total)
