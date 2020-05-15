num = int(input('How many numbers of the fibonacci sequence would you like to print? '))
sequence = [0, 1]

for x in range(num - 2):
    sequence.append(sequence[x] + sequence[x + 1])

print(*sequence, sep=", ")
