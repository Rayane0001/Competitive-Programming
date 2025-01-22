import re
p = re.compile(r'^(MIT(IT)*)+$')

for _ in range(int(input())):
    le = int(input())
    text = str(input())

    if p.match(text):
        print("YES")
    else:
        print("NO")
