from multiprocessing.pool import Pool
import time


start_time = time.time()


def cal_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num


p = Pool(processes=16)
num_range = range(2,10**6)
prime_list = p.map(cal_prime, num_range)
p.close()
p.join()
prime_list_clear = [2]+[x for x in prime_list if x is not None]

t = 1
while True:
    a = pow((prime_list_clear[t]-1), t, prime_list_clear[t]**2)
    b = pow((prime_list_clear[t]+1), t, prime_list_clear[t]**2)
    if (a + b) % prime_list_clear[t]**2 > 10**10:
        print(t)
        break
    t += 1


print('time:'+str(time.time()-start_time))
