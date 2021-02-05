import sys

s = sys.argv[1].split()
n = 0
result = "0"
for i in s:
    i = int(i)
    if i > n:
        n = i
        result = "1"
    else:
        result = "0"
        break
print(result)