for _ in range(int(input())):
	n=int(input())
	a = list(map(int, input().split()))

	even = sum(1 for i in a if i%2==0)
	odd = 2 * n - even
	
	if even == odd:
		print("YES")
	else:
		print("NO")