def find_next(a, b):
    return 2 * b + a, a + b

x1, x2 = 3, 2

sum = 0
for i in range(1, 1000):
    x1, x2 = find_next(x1, x2)
    if len(str(x1)) > len(str(x2)):
        sum += 1
print(sum)
