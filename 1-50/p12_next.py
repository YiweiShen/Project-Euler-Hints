import math


def cal_divisor_num(num):
    sum = 0
    for a in range(1, int(math.sqrt(num)) + 1):
        if num % a == 0:
            sum += 1
    return sum * 2


def generate__next_triangle_num(previous_num, sum):
    return sum + previous_num + 1


if __name__ == '__main__':
    b = 1
    for a in range(1, 99999999):
        b = generate__next_triangle_num(a, b)
        print(str(b) + ':' + str(cal_divisor_num(b)))
        if cal_divisor_num(b) > 500:
            print(str(b) + ':' + str(cal_divisor_num(b)))
            break
