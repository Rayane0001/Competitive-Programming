# k : dragons who got punched with a frying pan
k = int(input())
# l : the dragon got his tail shut into the balcony door
l = int(input())
# m : paws trampled with sharp heels
m = int(input())
# n : withdrew in panic
n = int(input())
# d : number of dragons
d = int(input())

damaged = 0
for i in range(1, d + 1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        damaged += 1

print(damaged)