s_file = open("numbers.txt")
s = s_file.read().split()
s = list(map(int, s))
z = 0
for i in s:
    if i < 0:
        z += i
s_file.close()
print(z)
