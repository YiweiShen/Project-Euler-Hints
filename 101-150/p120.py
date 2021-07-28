def f(a, n):
    return ((a+1)**n + (a-1)**n) % (a**2)

def try_it(a):
    max = 0
    for i in range(1, 2000):
        if f(a, i) > max:
            max = f(a, i)
    return max

if __name__ == '__main__':
    sum = 0
    for i in range(3, 1001):
        print(i)
        sum += try_it(i)
    print(sum)
