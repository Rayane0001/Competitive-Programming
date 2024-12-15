# tags: strings

n = int(input())
words = [input().strip() for _ in range(n)]

for i in range(n):
    if len(words[i]) > 10:
        between = len(words[i]) - 2
        new_word = f"{words[i][0]}{between}{words[i][-1]}"
        words[i] = new_word

for word in words:
    print(word)