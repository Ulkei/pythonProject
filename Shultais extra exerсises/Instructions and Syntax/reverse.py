import sys

a = sys.argv[1:]
a = " ".join(a)
a = list(a)
a.reverse()
a = "".join(a).split()
a = a[::-1]
a = " ".join(a)
print(a)
