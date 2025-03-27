import sys

n_str =sys.stdin.readline()
b_str=sys.stdin.readline().strip()

g= int(b_str,2)

k = g
mask= k>> 1
while mask != 0:
    k = k^ mask
    mask = mask >>1

position = k +1

print(position)
