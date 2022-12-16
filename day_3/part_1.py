input = open('input.txt').read().splitlines()

priorities = [
    chr(x) for x in list(range(ord('a'), ord('z') + 1)) + list(range(ord('A'), ord('Z') + 1))
]

overlap = []
for row in input:
    a = row[:len(row) // 2]
    b = row[len(row) // 2:]
    overlap.append(set(a) & set(b))

print(sum(priorities.index(x.pop()) + 1 for x in overlap))