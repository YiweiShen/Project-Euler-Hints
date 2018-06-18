def cal_collatz(x):
    if x % 2 == 0:
        return int(x / 2)
    return int(x * 3 + 1)


def collatz_time(x):
    sum = 1
    if x != 1:
        sum += collatz_time(cal_collatz(x))
    return sum


if __name__ == '__main__':
    max = 1
    for i in range(1, 1000000):
        if max < collatz_time(i):
            max = collatz_time(i)
            print(str(i) + ':' + str(max))
