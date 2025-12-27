for _ in range(int(input())):
    s = list(map(int, input().split()))

    winner1 = max(s[0], s[1])
    winner2 = max(s[2], s[3])

    s_s = sorted(s)

    if winner1 in s_s[2:] and winner2 in s_s[2:]:
        print("YES")
    else:
        print("NO")