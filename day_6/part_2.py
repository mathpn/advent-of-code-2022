input = open("input.txt").read()

for i in range(0, len(input) - 14):
    chars = input[i:i + 14]
    if len(chars) == len(set(chars)):
        break

print(i + 14)
