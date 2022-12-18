input = open("input.txt").read().splitlines()

pairs = []
supersets = 0
for row in input:
    pair_1, pair_2 = row.split(",")
    pair_1 = list(map(int, pair_1.split("-")))
    pair_2 = list(map(int, pair_2.split("-")))
    if (
        pair_1[0] <= pair_2[0] and pair_1[1] >= pair_2[1]
        or pair_2[0] <= pair_1[0] and pair_2[1] >= pair_1[1]
    ):
        supersets += 1

print(supersets)
