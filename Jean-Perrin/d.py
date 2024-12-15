def find_prefix():
    N, M, L = map(int, input().split())
    words = [input().strip() for _ in range(N)]
    words.sort()

    prefix_count = {}
    for word in words:
        if len(word) < L:
            continue
        prefix = word[:L]
        prefix_count[prefix] = prefix_count.get(prefix, 0) + 1

    valid_prefixes = [p for p in prefix_count if prefix_count[p] >= M]
    print(min(valid_prefixes) if valid_prefixes else 0)

find_prefix()