print("How many numbers of the fibonacci sequence (after the first two numbers) would you like to print?")
num = input()
num = int(num)
sequence = [0, 1]

for x in range(num):
    sequence.append(sequence[x]+sequence[x+1])

print(*sequence, sep=", ")