# tags: implementation, strings

word1 = input().strip()
word2 = input().strip()

if list(reversed(word1)) == list(word2):
    print("YES")
else:
    print("NO")