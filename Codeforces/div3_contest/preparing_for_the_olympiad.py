test_cases = int(input())

max_differences = []
for _ in range(test_cases):
    num_days = int(input())
    monocarp_problems = list(map(int, input().split()))
    stereocarp_problems = list(map(int, input().split()))

    max_diff_from_day = [0] * (num_days + 1)

    for day in range(num_days - 1, -1, -1):
        net_gain_today = monocarp_problems[day] - (stereocarp_problems[day + 1] if day + 1 < num_days else 0)
        max_diff_from_day[day] = max(max_diff_from_day[day + 1], net_gain_today + max_diff_from_day[day + 1])

    max_differences.append(max_diff_from_day[0])

print("\n".join(map(str, max_differences)))