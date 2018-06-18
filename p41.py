import time
from multiprocessing.pool import Pool


def is_prime(num):
    print(num)
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num


def is_pandigital(num_list):
    return len(list(set(num_list))) == len(num_list) and set(num_list) == set(list(str(1234567)))



if __name__ == '__main__':

    t = time.time()
    p = Pool(processes = 100)
    num_list = range(1234567, 7654322)
#    num_list = range(1234, 4322)
    prime_list = p.map(is_prime, num_list)
    p.close()
    p.join()
    prime_list_clear = [x for x in prime_list if x is not None]
    print(prime_list_clear)
    p_max = 0
    for i in prime_list_clear:
        if is_pandigital(list(str(i))):
            if i > p_max:
                p_max = i
    print(p_max)
    print('time:'+str(time.time()-t))
