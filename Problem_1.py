def feed_cows(N, M, cow_heights, candy_heights):
    cow_heights.sort()
    candy_heights.sort()

    result = [0] * N
    current_candy = 0

    for i in range(N):
        while current_candy < M and candy_heights[current_candy] <= cow_heights[i]:
            result[i] += candy_heights[current_candy]
            current_candy += 1

    return result

# Input reading
N, M = map(int, input().split())
cow_heights = list(map(int, input().split()))
candy_heights = list(map(int, input().split()))

# Simulate the process
result = feed_cows(N, M, cow_heights, candy_heights)

# Output
for i in range(N):
    print(result[i] + cow_heights[i])
#randomcommit