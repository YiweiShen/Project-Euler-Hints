import time

def factorial(x):
    product = 1
    for i in range(x):
        product = product * (i + 1)
    return product


def cal_combination(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))


def check():
    sum = 0
    for n in range(1, 101):
        for i in range(1, n+1):
            print(i)
            if cal_combination(n,i) > 1000000:
                sum += 1
    return sum


if __name__ == '__main__':
    t = time.time()
    print(check())
    print('time:'+str(time.time()-t))
