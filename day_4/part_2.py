input = open("input.txt").read().splitlines()

pairs = []
overlaps = 0
for row in input:
    pair_1, pair_2 = row.split(",")
    pair_1 = list(map(int, pair_1.split("-")))
    pair_2 = list(map(int, pair_2.split("-")))
    if not (pair_1[1] < pair_2[0] or pair_1[0] > pair_2[1]):
        overlaps += 1

print(overlaps)
