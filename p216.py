from multiprocessing.pool import Pool
import time

t =time.time()
LIMIT_NUM = 5*(10**7)


def is_prime(n):
    print(n)
    num = 2*n*n-1 # t(n)
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return 0
    return 1


p = Pool(processes=8)
num_range = range(2, LIMIT_NUM)
result_list = p.map(is_prime, num_range)
p.close()
p.join()
print(sum(result_list))


print('time:'+str(time.time()-t))
