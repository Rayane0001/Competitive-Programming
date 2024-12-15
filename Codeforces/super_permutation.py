q = int(input().strip())
results = []
for _ in range(q):
    n = int(input().strip())
    if n == 1:
        results.append("1")
        continue
    if n % 2:
        results.append("-1")
    else:
        result = []
        for i in range(1, n + 1):
            if i % 2 == 0:
                result.append(str(i - 1))
            else:
                result.append(str(i + 1))
        results.append(" ".join(result))

for result in results:
    print(result)