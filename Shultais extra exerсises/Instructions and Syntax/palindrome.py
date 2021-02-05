import sys

word = sys.argv[1]
word = list(word)
drow = word[::-1]
if word == drow:
    print("1")
else:
    print("0")



