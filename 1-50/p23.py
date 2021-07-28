from multiprocessing.pool import Pool

def is_abundant(num):
    return cal_divisor_sum(num) > num


def cal_divisor_sum(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum


def cal_abundant_list(num):
    print(num)
    if is_abundant(num):
        return num
    return None


def cal_result(num):
    print(num)
    for j in range(1, int(num/2+1)):
        if j in l_clean and (num-j) in l_clean:
            return None
    return num


if __name__ == '__main__':
    p = Pool(processes=100)

    nums = range(1, 28123)

    l = p.map(cal_abundant_list, nums)
    p.close()
    p.join()
    l_clean = [x for x in l if x is not None]
    print(l_clean)

    p = Pool(processes=100)
    r = p.map(cal_result, nums)
    p.close()
    p.join()
    r_clean = [x for x in r if x is not None]
    print(r_clean)
    print(sum(r_clean))
