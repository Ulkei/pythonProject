import sys

number = int(sys.argv[1])
i = 0
for i in range(1, 10):
    print(f'{number:d} x {i:d} = {number * i:d}')
    i += 1
