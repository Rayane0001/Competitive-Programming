# tags: implementation

# TODO : à refaire
number = input().strip()

lucky_count = sum(1 for digit in number if digit in '47')

if all(digit in '47' for digit in str(lucky_count)):
    print("YES")
else:
    print("NO")