from multiprocessing.pool import Pool
import time


start_time = time.time()
PRIME_NUM_WE_NEED = 10**6


def cal_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num


def is_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True


def check(num):
    if len(set(list(str(num)))) == len(list(str(num))):
        pass

p = Pool(processes=8)
num_range = range(2, PRIME_NUM_WE_NEED)
prime_list = p.map(cal_prime, num_range)
p.close()
p.join()
prime_list_clear = [x for x in prime_list if x is not None]
print(prime_list_clear)


print('time:'+str(time.time()-start_time))


for i in prime_list_clear:
    print(i)
    if check(i):
        print(i)
        break
