def min_days(N, heights, growth_rates, condition):
    days = 0

    while True:
        satisfied = True
        new_heights = []

        for i in range(N):
            new_height = heights[i] + days * growth_rates[i]
            new_heights.append(new_height)

        for i in range(N):
            taller_plants = sum(1 for j in range(N) if j != i and new_heights[j] > new_heights[i])
            if taller_plants != condition[i]:
                satisfied = False
                break

        if satisfied:
            return days

        days += 1

        if days > 2 * max(heights):
            return -1

T = int(input())

for _ in range(T):
    N = int(input())
    heights = list(map(int, input().split()))
    growth_rates = list(map(int, input().split()))
    condition = list(map(int, input().split()))

    result = min_days(N, heights, growth_rates, condition)
    print(result)
