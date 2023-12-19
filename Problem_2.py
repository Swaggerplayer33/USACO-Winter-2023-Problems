def min_starting_infected_cows(N, bitstring):
    min_infected_cows = float('inf')

    for i in range(N):
        nights_needed = max(i, N - 1 - i)
        infected_cows = int(bitstring[i]) + nights_needed
        min_infected_cows = min(min_infected_cows, infected_cows)

    return min_infected_cows

# This is how the program reads the input
N = int(input())
bitstring = input().strip()

if '0' not in bitstring:
    print(1)
else:
    result = min_starting_infected_cows(N, bitstring)
    print(result)
# Prints result