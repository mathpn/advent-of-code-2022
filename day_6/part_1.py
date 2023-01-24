input = open("input.txt").read()

for i in range(0, len(input) - 4):
    chars = input[i:i + 4]
    if len(chars) == len(set(chars)):
        break

print(i + 4)
