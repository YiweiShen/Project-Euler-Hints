import math


def is_curious(num):
    sum = 0
    for i in list(str(num)):
        sum += math.factorial(int(i))
    return num == sum


if __name__ == '__main__':
    cu_num = 0
    for i in range(10, 9999999):
        print(i)
        if is_curious(i):
            cu_num += i
    print(cu_num)

