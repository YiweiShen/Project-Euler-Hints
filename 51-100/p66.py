def diophantine(n):
    t = 2
    while True:
        k = ((t*t-1)/n)**0.5
        if k == int(k):
            return t
        t += 1
        print(t)

result_list = []

for i in range(5, 1001):
    print(i)
    result_list.append(diophantine(i))


print(max(result_list))
