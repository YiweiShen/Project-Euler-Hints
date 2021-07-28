import math


def cal_reciprocal_lenth(num):
    l = []
    x = 10**int(math.log10(num)+1)
    while True:
        m = x % num
        if m == 0:
            return 1
        if m in l:
            return len(l)+1
        l.append(m)
        x = m
        while True:
            if x > num:
                break
            x *= 10


if __name__ == '__main__':
    max = 2
    for i in range(19, 1000):
        a = cal_reciprocal_lenth(i)
        if a > max:
            max = a
            print(i)

