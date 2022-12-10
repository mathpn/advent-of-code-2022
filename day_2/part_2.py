input = open('input.txt').read().splitlines()

choices = ["A", "B", "C"]
strategies = [row.split(' ') for row in input]

total = 0
for oponent, mine in strategies:
    oponent = choices.index(oponent)
    if mine == "Y":
        mine = oponent + 1
        total += 3
    elif mine == "X":
        mine = (3 + oponent - 1) % 3 + 1
    elif mine == "Z":
        mine = (3 + oponent + 1) % 3 + 1
        total += 6
    total += mine

print(total)