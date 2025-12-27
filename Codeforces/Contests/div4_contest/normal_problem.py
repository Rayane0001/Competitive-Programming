# tags: implementation, strings

t = int(input())
for _ in range(t):
    a = input()
    translation_table = str.maketrans("pq", "qp")
    b = a[::-1].translate(translation_table)
    print(b)