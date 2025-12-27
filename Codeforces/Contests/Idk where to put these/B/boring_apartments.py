for _ in range(int(input())):
    x = input().strip() # apartment number
    d=int(x[0]) # first digit
    l=len(x) # apartment number length
    total = 10*(d-1)+l*(l+1)//2
    print(total)