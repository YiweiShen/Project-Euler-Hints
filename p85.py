def fn(a, b):
    sum =0
    for bx in range(b, 0, -1):
        for ax in range(a, 0, -1):
            sum += bx * ax
    return sum

dict_a = {}
for i in range(1, 110):
    print(i)
    for j in range(1, 110):
        dict_a[i,j] = fn(i, j)

min_gap = 1000000

print(dict_a)

for i, j in dict_a.items():
    if abs(j-2*10**6)< min_gap:
        print(i)
        min_gap = abs(j-2*10**6)
