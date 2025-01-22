N,K = map(int,input().split())
sc = [(*map(int, input().split()),i +1) for i in range(N)]
sc.sort(key=lambda x: x[:K])

for i in range(N -1):
    if any(sc[i][j] > sc[i + 1][j] for j in range(K)):
        print("NO")
        exit()

print("YES")
print(*[s[-1] for s in sc])
