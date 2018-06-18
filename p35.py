import time
from multiprocessing.pool import Pool


def is_prime(num):
    print(num)
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return None
    return num


def is_rotable(num):
    print(num)
    for i in range(0, len(str(num))):
        rotated_num = int(str(num)[i:] + str(num)[:i])
        if rotated_num not in prime_list_clear:
            return None
    return num



if __name__ == '__main__':
    t = time.time()
    p = Pool(processes = 100)
    num_range = range(2, 10**6)
    prime_list = p.map(is_prime, num_range)
    p.close()
    p.join()
    prime_list_clear = [x for x in prime_list if x is not None]

    p = Pool(processes = 100)
    result_list = p.map(is_rotable, prime_list_clear)
    result_list_clear = [x for x in result_list if x is not None]

    print(len(result_list_clear))
    print('time:'+str(time.time()-t))
