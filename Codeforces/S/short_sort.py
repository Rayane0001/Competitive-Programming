for _ in range(int(input())):
    s = input().strip()
    if s == "abc":
        print("YES")
    elif s == "acb" or s == "bac" or s == "cba":
        print("YES")
    else:
        print("NO")
