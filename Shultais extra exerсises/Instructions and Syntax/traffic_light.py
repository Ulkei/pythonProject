import sys

green = int(sys.argv[1])
yellow = int(sys.argv[2])
red = int(sys.argv[3])
time = int(sys.argv[4])
all_time = time % (green + yellow + red)

if all_time < green:
    print('green')
if green + yellow > all_time >= green:
    print('yellow')
if all_time >= green + yellow:
    print('red')

