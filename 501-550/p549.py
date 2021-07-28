from multiprocessing.pool import Pool
import time
import math

start_time = time.time()

def s(n):
    print(n)
    return max(divisors(n))


def divisors(n):
    divs = []
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            divs.append(n/i)
    if divs == []:
        divs.append(n)
    return list(divs)


def cal_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num

p = Pool(processes=8)
num_range = range(2,10**6)
prime_list = p.map(cal_prime, num_range)
p.close()
p.join()
prime_list_clear = [x for x in prime_list if x is not None]
print(prime_list_clear)


num_range = range(2, 10**2+1)
p = Pool(processes=8)
sum_list = p.map(s, num_range)
p.close()
p.join()

print(sum(sum_list))

print('time:'+str(time.time()-start_time))
