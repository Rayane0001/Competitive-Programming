from collections import Counter

def max_score(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        count = Counter(a)
        score = 0
        for frequency in count.values():
            score += frequency // 2
        results.append(score)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = max_score(t, test_cases)
for res in results:
    print(res)
