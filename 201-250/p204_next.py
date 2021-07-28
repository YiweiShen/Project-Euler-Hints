import time
import math
from multiprocessing.pool import Pool

LIMIT = 10**9
start_time = time.time()

def cal_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num

p = Pool(processes=8)
num_range = range(2,101)
prime_list = p.map(cal_prime, num_range)
p.close()
p.join()
prime_list_clear = [x for x in prime_list if x is not None]
print(prime_list_clear)


def recur(start, product, total):
    if product < LIMIT:
        total += 1
        for i in range(start, len(prime_list_clear)):
            total = recur(i, product*prime_list_clear[i], total)
    return total

print(recur(0,1,0)+1)
print('time:'+str(time.time()-start_time))
