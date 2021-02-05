f = open('run.txt')

first_list = []
for i in f.readlines():
    first_list.append(int(i.strip("\n")))

second_list = []
for i in range(len(first_list) - 2):
    if len(first_list[i:i + 5]) == 5:
        second_list.append(sum(first_list[i:i + 5]))
    else:
        break

best_time = min(second_list)
m = str(best_time // 60)
s = str(best_time % 60)

if len(m) == 1:
    m = "0" + m
if len(s) == 1:
    s = "0" + s

print(f"{m}:{s}")