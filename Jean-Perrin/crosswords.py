n,a=map(int,input().split())
m,b=map(int,input().split())
v=[input() for _ in range(a)]
h=[input() for _ in range(b)]
S=set(v)
import itertools
c=0
for rows in itertools.product(h,repeat=n):
    for j in range(m):
        if "".join(rows[i][j] for i in range(n)) not in S:
            break
    else:
        c+=1
print(c)
