def min_starting_cows(N, bitstring):
    min_start = float('inf')

    for i in range(N):
        current_bitstring = ['0'] * N
        current_bitstring[i] = '1'  #This is for the first infected cow

        for j in range(1, N):
            if bitstring[(i - j) % N] == '1':
                current_bitstring[(i - j) % N] = '1'
            if bitstring[(i + j) % N] == '1':
                current_bitstring[(i + j) % N] = '1'

        if ''.join(current_bitstring) == bitstring:
            min_start = min(min_start, current_bitstring.count('1'))

    return min_start

N = int(input())
bitstring = input().strip()

result = min_starting_cows(N, bitstring)
print(result)
#Print result :)