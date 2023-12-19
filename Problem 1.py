def feed_cows(N, M, cow_heights, candy_canes):
    cow_heights.sort(reverse=True)

    for candy_height in candy_canes:
        for i in range(N):
            if cow_heights[i] <= candy_height:
                cow_heights[i] += candy_height
                break

    return cow_heights

N, M = map(int, input().split())
cow_heights = list(map(int, input().split()))
candy_canes = list(map(int, input().split()))

result = feed_cows(N, M, cow_heights, candy_canes)

for height in result:
    print(height)
