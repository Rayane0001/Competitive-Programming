t = int(input())

for _ in range(t):
    total_kilometers, first_kilometers, second_kilometers, third_kilometers = map(int, input().split())
    kilometers = [first_kilometers, second_kilometers, third_kilometers]

    cycle_sum = sum(kilometers)

    full_cycles = total_kilometers // cycle_sum

    day = full_cycles * 3
    ran_kilometers = full_cycles * cycle_sum

    for i in range(3):
        if ran_kilometers >= total_kilometers:
            break
        ran_kilometers += kilometers[i]
        day += 1

    print(day)
