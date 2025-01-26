for _ in range(int(input())):
	h,m=map(int,input().split())
	
	h= h * 60
	print((24*60)-(m+h))