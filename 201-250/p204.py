import time
import math
from multiprocessing.pool import Pool


start_time = time.time()

def original_primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            for n in range(i+i, limit, i):     # Mark factors non-prime
                a[n] = False
    return a


def primes_sieve(num_range, primes, prime_bound):
    a = [True] * num_range                          # Initialize the primality list
    for (i, isprime) in enumerate(a):
        print(i)
        if i < prime_bound+1:
            continue
        else:
            if primes[i]:
                for n in range(i, num_range, i):     # Mark factors non-prime
                    if a[n]:
                        a[n] = False
    return a


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

plist = original_primes_sieve(10**9)
k = primes_sieve(10**9, plist, 100)

print(sum(k))  # minus 1 for 0 and plus 1 for the last number

print('time:'+str(time.time()-start_time))
