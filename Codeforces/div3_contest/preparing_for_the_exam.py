t = int(input())

results = []
for _ in range(t):
    # n : nb questions
    # m : nb absent questions
    # k : nb known questions
    n, m, k = map(int, input().split())

    absent_questions = list(map(int, input().split()))
    known_questions = set(map(int, input().split()))

    unknown_questions = set(range(1, n + 1)) - known_questions

    result = []
    for q in absent_questions:
        if len(unknown_questions - {q}) == 0:
            result.append("1")
        else:
            result.append("0")

    results.append("".join(result))

print("\n".join(results))
