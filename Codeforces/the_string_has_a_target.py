for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    min_char = min(s)
    min_index = s.rfind(min_char)

    print(s[min_index] + s[:min_index] + s[min_index+1:])