n, k = map(int, input().split())
scores = list(map(int, input().split()))

k_th_score = scores[k-1]

advancing = sum(1 for score in scores if score >= k_th_score and score >0)

print(advancing)