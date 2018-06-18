

for a in range(2,10**5):
    print(a)
    for b in range(1, a):
        x = (a*a + b*b)/2
        y = (a*a - b*b)/2
        if x == int(x) and y == int(y):
            for i in range(1, int(y)):
                k = (x+i)**0.5
                j = (y+i)**0.5
                m = (x-i)**0.5
                n = (y-i)**0.5
                if k == int(k) and j == int(j) and m == int(m) and n == int(n):
                    print(x)
                    print(y)
                    print(i)
                    break
