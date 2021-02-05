import sys

s = sys.argv[1].split()
lst = []
for item in s:
    lst.append(int(item))

variant_trend = []
max_trend = []

for j in range(0, len(lst)-1):
    l = lst[j:]
    i = 0
    while l[i + 1] > l[i]:
        variant_trend.append(l[i])
        i += 1
        variant_trend.append(l[len(variant_trend)])
    if len(variant_trend) > len(max_trend):
        max_trend = variant_trend
        variant_trend = []
    i = 0
    while l[i + 1] < l[i]:
        variant_trend.append(l[i])
        i += 1
    variant_trend.append(l[len(variant_trend)])
    if len(variant_trend) > len(max_trend):
        max_trend = variant_trend
        variant_trend = []
print(max_trend)