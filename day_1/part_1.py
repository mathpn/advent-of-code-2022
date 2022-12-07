input = open("./input.txt").read().splitlines()

elfs = []
elf = []
for row in input:
    if not row:
        elfs.append(sum(elf))
        elf = []
        continue
    elf.append(int(row))

elfs.append(sum(elf))
print(sorted(elfs)[-1])
