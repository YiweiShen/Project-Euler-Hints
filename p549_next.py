from multiprocessing.pool import Pool
import time
import math

start_time = time.time()
cache_dic = {}


def s(n):
    if n in prime_list_clear:
        return n
    t = 2
    try:
        return cache_dic[n]
    except:
        while math.factorial(t) % n != 0:
            t += 1
        cache_dic[n] = t
    return t


def c(n):
    print(n)
    if n in prime_list_clear:
        return n
    t = []
    for key, value in d(n).items():
        t.append(s(key)*value)
    return max(t)


def d(n):
    divs = {}
    num = n
    product = 1
    i = 2
    while num ** 0.5 > i:
        while num % i == 0:
            try:
                divs[i] += 1
            except:
                divs[i] = 1
            num /= i
        i += 1
    for key, value in divs.items():
        product = key ** value
    divs[int(n/product)] = 1
    return divs


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
sum_list = p.map(c, num_range)
p.close()
p.join()
print(sum_list)
print(sum(sum_list))


print('time:'+str(time.time()-start_time))


# too slow
