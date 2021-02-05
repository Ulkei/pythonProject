import sys

line_str = sys.argv[1]
line_str = line_str.split()
line = [int(x) for x in line_str]
x = max(line)
line.remove(x)
line.insert(0, x)
lines = [str(x) for x in line]
line2 = ' '.join(lines)

print(line2)
