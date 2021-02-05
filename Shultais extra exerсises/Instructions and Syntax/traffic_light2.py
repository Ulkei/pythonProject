import sys
d_a = list(map(int, sys.argv[1:5]))
print("green" if d_a[2] % (d_a[0] + d_a[1]) < d_a[0] else "red")