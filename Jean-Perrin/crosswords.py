import sys

def build_prefix_set(words):
    prefixes = set()
    for word in words:
        for i in range(1, len(word) + 1):
            prefixes.add(word[:i])
    return prefixes

def count_boards(n, m, vertical_words, horizontal_lines):
    prefix_set = build_prefix_set(vertical_words)
    count = 0
    board = []

    def backtrack(row_index):
        nonlocal count
        if row_index == n:
            for j in range(m):
                col = ''.join(board[i][j] for i in range(n))
                if col not in vertical_words:
                    return
            count += 1
            return

        for line in horizontal_lines:
            valid = True
            for j in range(m):
                vertical_prefix = ''.join(board[i][j] for i in range(row_index)) + line[j]
                if vertical_prefix not in prefix_set:
                    valid = False
                    break
            if valid:
                board.append(line)
                backtrack(row_index + 1)
                board.pop()

    backtrack(0)
    return count

data = sys.stdin.read().splitlines()
it = iter(data)
n, a = map(int, next(it).split())
m, b = map(int, next(it).split())
vertical_words = {next(it).strip() for _ in range(a)}
horizontal_lines = [next(it).strip() for _ in range(b)]

result = count_boards(n, m, vertical_words, horizontal_lines)
sys.stdout.write(str(result))