input = open('input.txt').read().splitlines()

priorities = [
    chr(x) for x in list(range(ord('a'), ord('z') + 1)) + list(range(ord('A'), ord('Z') + 1))
]

overlap = []
for i in range(0, len(input), 3):
    a = set(input[i])
    b = set(input[i + 1])
    c = set(input[i + 2])
    overlap.append(set(a) & set(b) & set(c))

print(sum(priorities.index(x.pop()) + 1 for x in overlap))