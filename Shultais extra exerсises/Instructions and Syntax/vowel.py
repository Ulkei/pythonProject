import sys

f = sys.argv[1]
total = []
for i in f:
    if i in "aeiouyAEIOUY":
        total.append(i)
print("".join(total))
