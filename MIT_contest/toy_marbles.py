n=int(input())
c=list(map(int,input().split()))
a=[]
v=[0]*n
p=[0]*n
for i in range(n):
    p[c[i]-1]=i
for i in range(n):
    while c[i]!=i+1:
        j=p[i]
        if c[j]!=j+1:
            a.append((1,i+1,j+1))
            c[i],c[j]=c[j],c[i]
            p[c[i]-1],p[c[j]-1]=i,j
        else:
            k=next((k for k in range(n) if c[k]==0),None)
            if k is None: break
            a.append((2,k+1,j+1))
            c[k]=c[j]
            c[j]=0
print(len(a))
for x in a:print(*x)
