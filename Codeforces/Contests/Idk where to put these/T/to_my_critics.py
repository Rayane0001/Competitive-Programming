for _ in range(int(input())):
    print("YES" if sum(sorted(map(int,input().split()))[-2:]) >= 10 else "NO")