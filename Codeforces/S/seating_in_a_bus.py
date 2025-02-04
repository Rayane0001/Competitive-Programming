for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    occupied = [False]*n

    occupied[a[0]-1]=True
    valid = True


    for seat in a[1:]:
        seat_index = seat-1
        if seat_index > 0 and occupied[seat_index-1] or seat_index<n-1 and occupied[seat_index+1]:
            occupied[seat_index] = True
        else:
            valid=False
            break

    if valid:
        print("YES")
    else:
        print("NO")