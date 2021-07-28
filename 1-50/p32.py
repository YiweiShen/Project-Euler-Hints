import time
from multiprocessing.pool import Pool


def is_pandigital(num_list):
    return len(list(set(num_list))) == len(num_list) and set(num_list) == set(list(str(123456789)))


def cal_multiplier(num):
    print(num)
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            if is_pandigital(list(str(i)+str(int(num/i))+str(num))):
                return num
    return None


if __name__ == '__main__':
    t = time.time()
    p = Pool(processes=100)
    nums = range(10**3, 10**6)
    result_list = p.map(cal_multiplier, nums)
    p.close()
    p.join()
    result_list_clear = [x for x in result_list if x is not None]
    print(result_list_clear)
    print(sum(result_list_clear))
    print('time:' + str(time.time() - t))
