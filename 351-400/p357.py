from multiprocessing.pool import Pool
import time

t =time.time()
LIMIT_NUM = 10**8

def cal_prime(num):
    print(num)
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
    print(num)
    for i in range(2, int(num**0.5)):
        if num % i == 0 and not is_prime(i+num/i):
            return False
    return num


p = Pool(processes=8)
num_range = range(2, LIMIT_NUM+1)
prime_list = p.map(cal_prime, num_range)
p.close()
p.join()
prime_list_clear = [x for x in prime_list if x is not None]
print(prime_list_clear)


sum_result = 0

for i in prime_list_clear:
    if check(i-1):
        sum_result += i-1

print(sum_result)

print('time:'+str(time.time()-t))
