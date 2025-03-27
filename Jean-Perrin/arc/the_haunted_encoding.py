import sys

n = int(sys.stdin.readline())
codes_l = [sys.stdin.readline().strip() for _ in range(n)]
codes_l = [c for c in codes_l if c]
n = len(codes_l)

if n == 0:
    print(0)
    sys.exit()

code_set = set(codes_l)
codes_sorted = sorted(codes_l)

max_len = 0
if codes_l:
    try:
        max_len = max(max(len(c) for c in codes_l), 1) if codes_l else 0
    except ValueError:
        max_len = 0

min_ambiguous = float('inf')
is_ambiguous = False
decodbl = {}

for i in range(n):
    p = codes_sorted[i]
    for j in range(i+1,n):
        q = codes_sorted[j]

        if q.startswith(p):
            is_ambiguous= True
            suffix = q[len(p):]

            if suffix:
                target_s1= suffix
                if target_s1 not in decodbl:
                    n_s1 =len(target_s1)
                    dp1= [False] * (n_s1+1)
                    dp1[0] =True
                    for i1 in range(1,n_s1 + 1):
                        for k1 in range(1, min(i1, max_len) + 1):
                            if dp1[i1-k1]:
                                cand1 =target_s1[i1-k1 : i1]
                                if cand1 in code_set:
                                    dp1[i1]= True
                                    break
                    decodbl[target_s1] = dp1[n_s1]

                if decodbl[target_s1]:
                    min_ambiguous = min(min_ambiguous, len(q))

            for c in code_set:
                if c.startswith(suffix):
                    rem = c[len(suffix):]
                    r_decodbl = False
                    if rem == "":
                        r_decodbl = True
                    elif rem:
                        target_s2 = rem
                        if target_s2 not in decodbl:
                            n_s2 =len(target_s2)
                            dp2 =[False]*(n_s2+1)
                            dp2[0] = True
                            for i2 in range(1,n_s2 +1):
                                for k2 in range(1, min(i2, max_len) + 1):
                                    if dp2[i2-k2]:
                                        cand2 = target_s2[i2-k2 : i2]
                                        if cand2 in code_set:
                                            dp2[i2]= True
                                            break
                            decodbl[target_s2] = dp2[n_s2]

                        r_decodbl= decodbl[target_s2]

                    if r_decodbl:
                        min_ambiguous =min(min_ambiguous,len(p)+len(c))
        else:
            break

if not is_ambiguous:
    print(0)
else:
    if min_ambiguous == float('inf'):
        print(0)
    else:
        print(min_ambiguous)